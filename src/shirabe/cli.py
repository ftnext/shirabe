import argparse
from pathlib import Path

from shirabe.deps import DependenciesCompiler
from shirabe.venv import ShirabeEnvBuilder


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dir",
        metavar="ENV_DIR",
        help="A directory to create the environment in.",
    )
    options = parser.parse_args()

    working_dir = Path.cwd()
    DependenciesCompiler(working_dir).run()

    builder = ShirabeEnvBuilder(with_pip=True)
    builder.create(options.dir)
