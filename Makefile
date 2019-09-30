# Ansible Deploy
deploy:
	rm -rf to-tmcd-me/node_modules
	rm -rf to-tmcd-me/dist
	rm -rf to-server-api/env
	# cd ./to-tmcd-me && npm install && npm run build
	ansible-playbook -i ansible/hosts -v ansible/site.yml
	# ssh-agent bash
	# ssh-add ~/.ssh/id_rsa

# Build frontend

# Migrate DB on remote: should only be run where the MySQL server is running

# Start up MySQL Server
