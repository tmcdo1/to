# Ansible Deploy
deploy:
	ssh-agent bash
	ssh-add ~/.ssh/id_rsa
	ansible -i ansible/hosts ansible/site.yml

# Build frontend

# Migrate DB on remote: should only be run where the MySQL server is running

# Start up MySQL Server
