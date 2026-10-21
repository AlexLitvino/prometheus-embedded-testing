import pytest


# Req 9
def test_no_response_becomes_timeout(device):
    with pytest.raises(TimeoutError):
        device.command("NO_RESPONSE")
