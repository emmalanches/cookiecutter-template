"""Defines constants for the Build such as PATH."""
from pathlib import Path

THIS_DIR = Path(__file__).parent
PROJECT_DIR = (THIS_DIR / "../").resolve()
