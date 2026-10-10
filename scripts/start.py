import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent


def resolve_target_dir(directory: str | None = None, cwd: Path | None = None) -> Path:
    """Resolve the directory that should be served for local theme previews."""
    base_dir = (cwd or Path.cwd()).resolve()

    if directory:
        candidate = Path(directory).expanduser()
        if not candidate.is_absolute():
            candidate = (base_dir / candidate).resolve()
        if candidate.exists():
            if candidate == REPO_ROOT or candidate == SCRIPT_DIR:
                repo_themes = REPO_ROOT / "themes"
                if repo_themes.exists():
                    theme_dirs = sorted(path for path in repo_themes.iterdir() if path.is_dir())
                    if len(theme_dirs) == 1:
                        return theme_dirs[0]
            return candidate
        raise FileNotFoundError(f"Directory does not exist: {candidate}")

    for candidate in [base_dir, *base_dir.parents]:
        theme_css = candidate / "theme.css"
        bundle_css = candidate / "bundle.min.css"
        if theme_css.exists() or bundle_css.exists():
            return candidate

    repo_themes = REPO_ROOT / "themes"
    if repo_themes.exists():
        theme_dirs = sorted(path for path in repo_themes.iterdir() if path.is_dir())
        if len(theme_dirs) == 1:
            return theme_dirs[0]

    if base_dir == REPO_ROOT or base_dir == SCRIPT_DIR:
        return REPO_ROOT

    return base_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve a Jellyfin theme locally.")
    parser.add_argument(
        "directory",
        nargs="?",
        help="Optional directory to serve instead of automatically detecting it.",
    )
    args = parser.parse_args()

    target_dir = resolve_target_dir(directory=args.directory)

    subprocess.Popen(
        [
            sys.executable,
            "-m",
            "http.server",
            "8787",
            "--bind",
            "0.0.0.0",
            "--directory",
            str(target_dir),
        ],
        cwd=str(target_dir),
    )


if __name__ == "__main__":
    main()