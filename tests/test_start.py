from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import start


class StartScriptTest(unittest.TestCase):
    def test_resolve_target_dir_from_theme_folder(self):
        theme_dir = ROOT / "themes" / "jellyfin-obsidian-material"
        self.assertEqual(start.resolve_target_dir(cwd=theme_dir), theme_dir)

    def test_resolve_target_dir_from_repo_root_prefers_theme(self):
        theme_dir = ROOT / "themes" / "jellyfin-obsidian-material"
        self.assertEqual(start.resolve_target_dir(cwd=ROOT), theme_dir)

    def test_resolve_target_dir_from_explicit_repo_directory(self):
        theme_dir = ROOT / "themes" / "jellyfin-obsidian-material"
        self.assertEqual(start.resolve_target_dir(directory=str(ROOT)), theme_dir)

    def test_resolve_target_dir_from_scripts_folder_prefers_theme(self):
        script_dir = ROOT / "scripts"
        theme_dir = ROOT / "themes" / "jellyfin-obsidian-material"
        self.assertEqual(start.resolve_target_dir(cwd=script_dir), theme_dir)


if __name__ == "__main__":
    unittest.main()
