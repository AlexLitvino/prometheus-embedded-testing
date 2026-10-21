import pytest


# Req 5
@pytest.mark.parametrize("value", [0, 1, 50, 99, 100])
def test_pwm_valid_boundaries(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "OK"
    assert r["pwm"] == value


# Req 6
@pytest.mark.parametrize("value", [-1, 101, 999])
def test_pwm_invalid_boundaries(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "ERROR"
    assert r["code"] == "INVALID_VALUE"


# Req 6
@pytest.mark.parametrize("value", [50.5, 1.2e1, "abc", "10 20", "!@#$%^"])
def test_pwm_invalid_values(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "ERROR"
    assert r["code"] == "INVALID_VALUE"
