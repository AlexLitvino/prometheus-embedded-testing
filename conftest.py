import os
import pytest
from device import Device


@pytest.fixture
def device():
    port = os.getenv("DEVICE_PORT")
    if not port:
        pytest.skip("Set DEVICE_PORT, e.g. COM5, /dev/ttyUSB0 or rfc2217://localhost:4000 (Wokwi)")
    dev = Device(port, timeout=2.0)  # increased to 2s because PING command has longer timeout than 1s
    yield dev
    try:
        dev.command("RESET")
    finally:
        dev.close()
