import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

subprocess.Popen(
    [
        sys.executable,
        "-m",
        "http.server",
        "8787",
        "--bind",
        "0.0.0.0",
        "--directory",
        str(ROOT),
    ],
    cwd=ROOT,
)