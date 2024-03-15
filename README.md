# djreact
Examples of integrating Django w/ React

Starting inside a VM built with Vagrant and populated by Git, install Python/Dango, Node/React, and NGINX to get a functioning demo that started with but has moved past the [DigitalOcean Tutorial](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react).

## Prerequsites:
* Git
* Vagrant
* A code editor
* A browser

## Getting Started
### Create, boot, and log in to your box
1. cd to an appropriate working directory
2. `git clone https://github.com/Ecotrust/djreact.git`
3. `cd djreact`
4. Review/edit/update the Vagrantfile to match your environment:
    * Are you an a Mac with M2 or M3 chips?
        * You likely are using QEMU instead of VirtualBox and probably will need a different VM image than `ubuntu/jammy64`
        * You likely need to use SMB for your shared directories
    * Is your working directory `/usr/local/apps/djreact`? If not, update your shared directories' locations
6. `vagrant up`
7. `vagrant ssh`

### Install Software
#### Python and Django
* Follow (this tutorial from DigitalOcean to set up Python 3)[https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-22-04-server]
   * Stop after step 2
   * For the current code, there may be assumptions that the virtual environment lives at `/usr/local/apps/env` (not `environments` or `my_env`). It's probable that this isn't important
   * Inside a VM with shared directories, it is helpful to make sure your env is NOT inside of the shared directory, as permission issues can occur
* Once your virtualenv is active, install the required libraries:
   * `pip install -r /usr/local/apps/djreact/django-todo-react/backend/requirements.txt`
   * `python /usr/local/apps/djareact/django-todo-react/backend/manage.py migrate`
   * `python /usr/local/apps/djareact/django-todo-react/backend/manage.py runserver 0:8000`
   * Leave this terminal open and running: do the rest in a new terminal
     * Be sure to use `vagrant ssh` again to ensure you're running on your VM rather than your host
    
#### Node and React
* There may be some missing pieces here: npm install react? How do we get npx and do we need to run it for node to recognize how to build this app?
* Follow (this tutorial from DigitalOcean to set up Node.js)[https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04#option-3-installing-node-using-the-node-version-manager] using the 'NVM' approach:
  * run `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`
  * `source ~/.bashrc`
  * `nvm install lts/iron`
* `npm install bootstrap reactstrap axios`
* `cd /usr/local/apps/djreact/django-todo-react/frontend`
* `npm build`

#### NGINX
* `sudo apt install nginx`
* `sudo cp /usr/local/apps/djreact/deploy/todo.nginx /etc/nginx/sites-available/todo`
* `sudo rm /etc/nginx/sites-enabled/default`
* `sudo ln -s /etc/nginx/sites-available/todo /etc/nginx/sites-enabled/`
* `sudo systemctl start nginx` <-- or maybe `restart`

## Test and Review
* open "http://localhost:8080" on your host machine -> do you get the React TODO app?
* open "http://localhost:8000" on your host machine -> do you get the Django template wrapped around the React TODO app?
