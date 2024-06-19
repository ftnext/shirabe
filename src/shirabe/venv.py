import os.path
from venv import EnvBuilder


class ShirabeEnvBuilder(EnvBuilder):
    def post_setup(self, context):
        env_dir = context.env_dir
        requirements_file = os.path.join(
            os.path.dirname(env_dir), "requirements.txt"
        )
        if os.path.exists(requirements_file):
            self._install_requirements(context, requirements_file)

    def _install_requirements(self, context, requirements_file):
        self._call_new_python(
            context,
            "-m",
            "pip",
            "install",
            "--no-deps",
            "-r",
            requirements_file,
        )


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dir",
        metavar="ENV_DIR",
        help="A directory to create the environment in.",
    )
    options = parser.parse_args()

    builder = ShirabeEnvBuilder(with_pip=True)
    builder.create(options.dir)
