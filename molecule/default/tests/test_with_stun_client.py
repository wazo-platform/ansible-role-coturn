import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("molecule-coturn-stun-client")


@pytest.mark.parametrize(
    "port",
    ["12345", "54321"],
)
def test_stun(host, port):
    matchers = ["My IP is  172", "My IP is  192"]
    cmd = host.check_output(
        "node /opt/stun/client.js {} {}".format("molecule-coturn-debian11", port)
    )
    assert any(match in cmd for match in matchers)
