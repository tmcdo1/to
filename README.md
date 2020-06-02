# to

> To is no longer in service. to.tmcd.me no longer exists.

To was a global aliasing tool that allows users to quickly access webpages. Think of it as a url shortner with an extension that adds functionality in browser for simple aliasing like `to/fb` in your browser searchbar.

It is important to note that all the variables in the Ansible setup are no longer in use and are now made publicly available, so change them!

# Deployment

An Ansible playbook is given to configure a server for usage. Be sure to modify the variables in the `ansible/group_vars` directory.

Feel free to modify the NGINX configuration etc. You should also change the host(s) in the `ansible/hosts` file to whatever your servers are.

Enjoy!
