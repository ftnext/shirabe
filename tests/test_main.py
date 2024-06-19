import subprocess
from unittest.mock import patch


@patch("shirabe.venv.ShirabeEnvBuilder._install_requirements")
def test_python_m_shirabe_no_requirements(
    _install_requirements, tmp_path, monkeypatch
):
    with monkeypatch.context() as m:
        m.chdir(tmp_path)
        subprocess.run(["python", "-m", "shirabe", ".venv"])

    _install_requirements.assert_not_called()
