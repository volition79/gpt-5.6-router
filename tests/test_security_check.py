from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SecurityCheckTests(unittest.TestCase):
    def copy_repository(self) -> Path:
        temp_root = Path(tempfile.mkdtemp(prefix="gpt56-router-security-")) / "repo"
        shutil.copytree(ROOT, temp_root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.addCleanup(shutil.rmtree, temp_root.parent, True)
        return temp_root

    def run_check(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", "scripts/security_check.py"],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_clean_repository_passes(self) -> None:
        result = self.run_check(self.copy_repository())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Security checks passed", result.stdout)

    def test_synthetic_secret_fails_without_echoing_value(self) -> None:
        root = self.copy_repository()
        synthetic = "gh" + "p_" + ("A" * 40)
        (root / "synthetic-leak.md").write_text(synthetic, encoding="utf-8")

        result = self.run_check(root)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("credential-like GitHub token", result.stderr)
        self.assertNotIn(synthetic, result.stdout + result.stderr)

    def test_missing_explicit_install_authority_fails(self) -> None:
        root = self.copy_repository()
        korean = root / "README.md"
        english = root / "README.en.md"
        korean.write_text(
            korean.read_text(encoding="utf-8").replace("설치 또는 업데이트 권한이 생기지 않습니다", "설치할 수 있습니다"),
            encoding="utf-8",
        )
        english.write_text(
            english.read_text(encoding="utf-8").replace("does not grant installation or update authority", "permits installation"),
            encoding="utf-8",
        )

        result = self.run_check(root)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("installation requires explicit authority", result.stderr)

    def test_mutable_install_target_fails(self) -> None:
        root = self.copy_repository()
        for name in ("README.md", "README.en.md"):
            path = root / name
            path.write_text(
                path.read_text(encoding="utf-8").replace("git clone --branch v1.0.1 --depth 1", "git clone"),
                encoding="utf-8",
            )

        result = self.run_check(root)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("installation pins release", result.stderr)

    def test_missing_reserved_namespace_guidance_fails(self) -> None:
        root = self.copy_repository()
        runtime = root / "references/runtime-troubleshooting.md"
        runtime.write_text(
            runtime.read_text(encoding="utf-8").replace("issue #31864", "issue removed"),
            encoding="utf-8",
        )

        result = self.run_check(root)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("reserved namespace workaround documented", result.stderr)


if __name__ == "__main__":
    unittest.main()
