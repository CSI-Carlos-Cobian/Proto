#!/bin/bash
sudo apt-get update 
sudo apt-get upgrade -y
sudo apt-get install python-dev default-libmysqlclient-dev python3-pip python-pip -y
sudo pip3 install inquirer
# django-extensions
# rest_framework_swagger

# https://pypi.org/project/drf-aggregates/

sudo apt install mysql-server -y
#TODO: Secure Configuration disabled. 
sudo mysql -e "CREATE USER 'protoapi'@'%' IDENTIFIED BY '4dHocHomeworkPr0t0' ; "
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'protoapi'@'%';"
sudo mysql -e "GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'protoapi'@'%' WITH GRANT OPTION;"
sudo mysql -e "FLUSH PRIVILEGES;"
sudo mysql -e "CREATE SCHEMA protoapi_db"


# sudo git clone https://github.com/carloscobian96/Proto.git --branch Python

cd Proto/api
sudo pip3 install -r requirements.txt
sudo python3 manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@adhoc.com', '4dHocHomeworkPr0t0')" | sudo python3 api/manage.py shell 
sudo python3 api/manage.py runserver &


sleep 10
sudo python3 Main.py