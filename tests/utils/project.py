import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

from tests.const import PROJECT_DIR


def initialise_git_repo(repo_dir: Path): 
    subprocess.run(["git", "init"], cwd=repo_dir, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "'feat: initial commit'"], cwd=repo_dir, check=True)


def generate_project(temp_values: Dict[str, str], test_session_id): 
    template_values: Dict[str,str] = deepcopy(temp_values)
    cookiecutter_config = {"default_context":template_values}
    cookiecutter_config_fpath = PROJECT_DIR / f"cookiecutter-{test_session_id}.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))
    
    cmd = [
        "cookiecutter", 
        str(PROJECT_DIR),
        "--output-dir", 
        str(PROJECT_DIR / "sample"), 
        "--no-input", 
        "--config-file", 
        str(cookiecutter_config_fpath)
    ]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)

    generated_project_dir = PROJECT_DIR / "sample" / cookiecutter_config["default_context"]["repo_name"]

    return generated_project_dir