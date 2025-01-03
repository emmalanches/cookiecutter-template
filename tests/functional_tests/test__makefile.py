import subprocess
from pathlib import Path

import pytest


def test__linting_passes(project_dir: Path): 
    """Runs lint-ci command to check linting."""
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)

def test__tests_pass(project_dir: Path): 
    """Installs and builds the wheel file to check it all builds correctly."""
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)