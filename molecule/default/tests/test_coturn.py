import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("molecule-coturn-debian11")


@pytest.mark.parametrize(
    "name", ["coturn"],
)
def test_packages(host, name):
    print(testinfra_hosts)

    item = host.package(name)
    assert item.is_installed


@pytest.mark.parametrize(
    "path",
    [
        "/etc/consul/consul.d/coturn-metrics.service.json",
        "/etc/consul/consul.d/coturn-ui.service.json",
        "/etc/default/coturn",
        "/etc/logrotate.d/rsyslog",
        "/etc/turnserver.conf",
        "/lib/systemd/system/coturn.service.d/user_group.conf",
    ],
)
def test_files(host, path):
    with host.sudo():
        item = host.file(path)
        assert item.exists


def test_group(host):
    g = host.group("turnserver")
    assert g.exists


def test_user(host):
    u = host.user("turnserver")
    assert u.exists


@pytest.mark.parametrize("name", ["coturn"])
def test_services(host, name):
    item = host.service(name)
    assert item.is_running
    assert item.is_enabled


def test_admin_ui(host):
    with host.sudo():
        cmd = host.check_output("curl http://localhost:9090/")
        assert "TURN" in cmd, cmd


# TODO enable when https://github.com/coturn/coturn/pull/517 is released (version > 4.5.1.3)
# def test_metrics(host):
#     with host.sudo():
#         cmd = host.check_output("curl http://localhost:9641/")
#         assert "# HELP turn_status" in cmd, cmd
