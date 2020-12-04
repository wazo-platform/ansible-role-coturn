# Ansible role coturn

Setup TURN/STUN server Coturn

This role is tested using [Molecule](https://molecule.readthedocs.io/). The default will use Docker that you must install yourself. Then run `tox` to setup python environment and start testing. If docker can't do, a Vagrant & libvirt (tested with KVM) is also possible, set up those then `tox -- test -s vagrant`.

A [Vagrantfile](https://www.vagrantup.com/) is also provided for development purpose. Install Vagrant and VirtualBox (or libvirt / KVM), then run `vagrant up`.

## Requirements

Python & [tox](https://tox.readthedocs.io). See imports in `library/*` and tasks in `molecule/default/converge.yml` if any specific, but those should be added in `tox.ini`.

## Role Variables

See [defaults/main.yml](defaults/main.yml).

## Dependencies

See [meta/main.yml](meta/main.yml) and [molecule/default/requirements.yml](molecule/default/requirements.yml) if any.

## Example Playbook

```yaml
- hosts: all
  vars:
    coturn_user: root
    coturn_group: root
    coturn_auth_mechanism: long-term
    coturn_users:
      - username: turnuser
        password: turnpassword
    coturn_realm: turnrealm
    coturn_alternative_listening_port: 80
    coturn_tls_enabled: false
    coturn_dtls_enabled: false
    coturn_tls_alternative_listening_port: 443
    coturn_web_admin_enabled: false
    coturn_web_admin_ip: 0.0.0.0
  roles:
    - wazo.coturn
```

## License

MIT

## Author Information

Wazo Developers for Wazo https://wazo.io
