import pytest

@pytest.fixture
def sample_lines():
    return [
        {"qty": 2, "unit_price": 19.99, "desc": "Widget"},
        {"qty": 1, "unit_price": 5.50, "desc": "Gadget"},
    ]
