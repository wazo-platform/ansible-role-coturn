import os

import pytest
import testinfra.utils.ansible_runner

runner = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
)
testinfra_hosts = runner.get_hosts("molecule-coturn-stun-client")

# The coturn container name embeds the Debian version under test
coturn_host = runner.get_hosts("molecule_coturn")[0]


@pytest.mark.parametrize(
    "port",
    ["12345", "54321"],
)
def test_stun(host, port):
    matchers = ["My IP is  172", "My IP is  192"]
    cmd = host.check_output(f"node /opt/stun/client.js {coturn_host} {port}")
    assert any(match in cmd for match in matchers)
