import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from config import DEFAULT_APP_NAME, DEFAULT_PORT
from utils import normalize_text, calculate_average


def test_normalize_text_trims_and_lowercases_text():
    assert normalize_text("   Hello   Python   Lab   ") == "hello python lab"


def test_calculate_average_sums_and_divides_values():
    assert calculate_average([10, 20, 30]) == 20


def test_default_project_configuration_values():
    assert DEFAULT_APP_NAME == "python_lab"
    assert DEFAULT_PORT == 8000
