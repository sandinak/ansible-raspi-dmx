# ansible-raspi-dmx
Ansible Playbooks to build out Raspi config for DMX stuff

- requires sshpass to get to the raspi unless you preconfigure with an ssh key.

## Operation
1. Need a base installation of Python and virtualenv 
2. cd into the directory
3. Run ```. sourceme```
4. Edit the inventory ```raspi``` file to match your hosting setup
5. use ansible-playbook to configure your host(s)
```
ansible-playbook playbooks/build/dmx_controllers.yml
```