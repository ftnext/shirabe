import subprocess
from pathlib import Path


class DependenciesCompiler:
    def __init__(self, work_dir: Path) -> None:
        self.work_dir = work_dir

    def run(self):
        if not (self.work_dir / "requirements.txt").exists():
            subprocess.run(["python", "-m", "piptools", "compile"])
