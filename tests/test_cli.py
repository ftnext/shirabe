import sys
from unittest.mock import ANY, patch

from shirabe.cli import main


def run_shirabe(venv_path):
    with patch.object(sys, "argv", ["shirabe", venv_path]):
        main()


@patch("shirabe.venv.ShirabeEnvBuilder._install_requirements")
@patch("shirabe.deps.click.Context.invoke")
def test_shirabe_with_resolved_dependencies(
    click_invoke, _install_requirements, tmp_path, monkeypatch
):
    requirements_file_path = tmp_path / "requirements.txt"
    requirements_file_path.write_text("kojo-fan-art==0.1.1")

    with monkeypatch.context() as m:
        m.chdir(tmp_path)
        run_shirabe(".venv")

    click_invoke.assert_not_called()
    _install_requirements.assert_called_once_with(
        ANY, str(requirements_file_path)
    )
