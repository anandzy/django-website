#!/bin/bash
#Django application Pre-requasits on ubuntu18.04 

#https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04

#git clone https://github.com/anandzy/django-website.git ~/mywebsite

#aws ami- ami-0ac019f4fcb7cb7e6 - ubuntu18.04


sudo apt update -y && sudo apt upgrade -y
ls
sudo apt update
python3 -V
udo apt install python3-pipsudo apt install python3-venv
sudo apt install python3-venv
cd mywebsite/
python3.6 -m venv my_env
source my_env/bin/activate
cd
pip install -e ~/mywebsite/
cd web
cd mywebsite/
pip install django
pip install requests
./manage.py runserver 0.0.0.0:80
