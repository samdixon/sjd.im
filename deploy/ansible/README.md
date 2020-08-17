### Intro
This folder contains all items related to ansible configuration management for sjd.im.

### Requirements
- ansible
- sshpass

### Development
For development of ansible scripts I like to use a completely fresh server to test from 0 to 100% of deploy. Any blank debian 10 server will work. I use digitalocean because it is easy for me. Simply add the blank server ip to the development file and run `ansible-playbook site.yml -i development` to do a full ansible deploy.




### Production Commands

##### User Init
`ansible-playbook site.yml -i production --tags "init"`

##### Deploys
`ansible-playbook site.yml -i production --skip-tags "init"`
