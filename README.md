# ansible-raspi-dmx
Ansible Playbooks to build out Raspi config for DMX stuff

- requires sshpass to get to the raspi unless you preconfigure with an ssh key.

## Notes
- Right now this requires a Mac environment for the build tool.  

## Operation
1. Need a base installation of Python and virtualenv ( ''' brew install python pyenv-virtualenv ''' )
2. clone this repo into a directory ```git clone https://github.com/sandinak/ansible-raspi-dmx```
3. ```cd ansible-raspi-dmx```
4. Run ```. sourceme```, this will run ```make``` to build out the virtual env
and setup your environment.
5. Edit the inventory ```raspi``` file to match your hosting setup
6. use ansible-playbook to configure your host(s)
```
ansible-playbook playbooks/build/dmx_controllers.yml
```

## Configuration
This configuration is setup for our current tour.  I'll make a more generic 
version of this moving forward and gilt in the work needed.  For now, you 
will want to setup groups thus:

- dmx_controllers - put any hosts in ths group will be setup to use the 
  https://www.bitwizard.nl/shop/DMX-interface-for-Raspberry-pi. 
  
- steps are setup to use raspi -> fadecandy controllers, where each step is 4 U 
  big

