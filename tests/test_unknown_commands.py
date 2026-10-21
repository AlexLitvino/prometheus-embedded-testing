# Req 8
def test_unknown_commands(device):
    r = device.command("UNKNOWN")
    assert r['status'] == 'ERROR'
    assert r['code'] == 'UNKNOWN_COMMAND'
