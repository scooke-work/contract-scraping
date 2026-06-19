"""Make the top-level modules importable from tests/ without installing a package."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
