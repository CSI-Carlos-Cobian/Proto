#!/bin/bash
sudo apt-get install python3 pip3 -y
# sudo apt-get install pip3 -y
sudo pip3 install inquirer
#sudo python3 Main.py

# https://pypi.org/project/drf-aggregates/

sudo apt install mysql-server -y
sudo mysql -e "CREATE USER 'protoapi'@'%' IDENTIFIED BY '4dHocHomeworkPr0t0' ; "
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'protoapi'@'%';"
sudo mysql -e "GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'protoapi'@'%' WITH GRANT OPTION;"
sudo mysql -e "FLUSH PRIVILEGES;"