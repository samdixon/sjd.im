full-deploy-dev:
	ansible-playbook site.yml -i development --tags "init" --private-key ~/.ssh/id_rsa

deploy-dev:
	ansible-playbook site.yml -i development --skip-tags "init" --tags "dev, deploy" --private-key ~/.ssh/id_rsa

deploy-prod:
	ansible-playbook site.yml -i production --skip-tags "init" --private-key ~/.ssh/id_rsa
