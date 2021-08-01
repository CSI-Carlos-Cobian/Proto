#!/bin/bash
sudo apt-get update 
sudo apt-get upgrade -y
sudo apt-get install python-dev default-libmysqlclient-dev python3-pip python-pip -y

sudo apt install mysql-server -y
# sudo mysql_secure_installation
sudo mysql -e "CREATE USER 'protoapi'@'%' IDENTIFIED BY '4dHocHomeworkPr0t0' ; "
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'protoapi'@'%';"
sudo mysql -e "GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'protoapi'@'%' WITH GRANT OPTION;"
sudo mysql -e "FLUSH PRIVILEGES;"
sudo mysql -e "CREATE SCHEMA protoapi_db"


cd api
sudo pip3 install -r requirements.txt
sudo python3 manage.py migrate
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@adhoc.com', '4dHocHomeworkPr0t0')" | sudo python3 manage.py shell 
cd ..