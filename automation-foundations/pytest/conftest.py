import pytest

@pytest.fixture
def bgp_data():
    return {
        "global": {
            "peers": {
                "10.0.0.2": {"is_up": True,  "remote_as": 65002},
                "10.0.0.3": {"is_up": False, "remote_as": 65003},
            }
        }
    }
