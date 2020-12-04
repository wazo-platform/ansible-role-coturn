import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("molecule-coturn-stun-client")


@pytest.mark.parametrize(
    "port", ["12345", "54321"],
)
def test_stun(host, port):
    cmd = host.check_output(
        "node /opt/stun/client.js {} {}".format("molecule-coturn-debian10", port)
    )
    assert "My IP is  172" in cmd, cmd
