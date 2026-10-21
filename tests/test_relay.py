# Req 4
def test_led_on_off(device):
    assert device.command("SET LED ON")["led"] is True
    assert device.command("SET LED OFF")["led"] is False


# Req 7
def test_reset_restores_safe_state_led(device):
    device.command("SET LED ON")
    device.command("RESET")
    status = device.command("STATUS")
    assert status["pwm"] == 0
    assert status["led"] is False


# Req 7
def test_reset_restores_safe_state_pwm(device):
    device.command("SET PWM 45")
    device.command("RESET")
    status = device.command("STATUS")
    assert status["pwm"] == 0
    assert status["led"] is False
