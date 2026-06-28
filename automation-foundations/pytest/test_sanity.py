



import pytest

@pytest.mark.parametrize("neighbor_ip", ["10.0.0.2", "10.0.0.3"])
def test_neighbor_up(bgp_data, neighbor_ip):
    assert bgp_data["global"]["peers"][neighbor_ip]["is_up"] is True
