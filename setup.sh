#!/bin/bash
sudo apt-get install python3 pip3 git -y
# sudo apt-get install pip3 -y
sudo pip3 install inquirer


# https://pypi.org/project/drf-aggregates/

sudo apt install mysql-server -y
sudo mysql -e "CREATE USER 'protoapi'@'%' IDENTIFIED BY '4dHocHomeworkPr0t0' ; "
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'protoapi'@'%';"
sudo mysql -e "GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'protoapi'@'%' WITH GRANT OPTION;"
sudo mysql -e "FLUSH PRIVILEGES;"
sudo mysql -e "CREATE SCHEMA protoapi_db"


# sudo git clone https://github.com/carloscobian96/Proto.git

cd Proto

sudo pip3 install -r api/requirements.txt
sudo python3 api/manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@adhoc.com', '4dHocHomeworkPr0t0')" | sudo python3 api/manage.py shell 
sudo python3 api/manage.py runserver &


sleep 10
sudo python3 Main.py

#sudo python3 Main.py