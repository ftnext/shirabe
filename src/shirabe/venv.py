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

    def _install_requirements(self, context, requirements_file: str):
        self._call_new_python(
            context,
            "-m",
            "pip",
            "install",
            "--no-deps",
            "-r",
            requirements_file,
        )

    def _call_new_python(self, context, *py_args, **kwargs):
        # Avoid for mypy to raise [attr-defined] error
        # >error: "ShirabeEnvBuilder" has no attribute "_call_new_python"
        return super()._call_new_python(context, *py_args, **kwargs)


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
