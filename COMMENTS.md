# Welcome to the Proto wiki!

## File parsing Application Interface Utilization:

### Update system and Clone Project
`sudo apt-get update`

`sudo apt-get upgrade -y`

`sudo apt-get install git -y`

`sudo git clone https://github.com/carloscobian96/Proto.git`

`cd Proto`

### Installs dependencies for data migration. 

`sudo sh setup.sh`

TODO: `mysql_secure_installation` has been disabled

TODO: Uncontainerized applications may cause configuration conflicts on standing systems.

### Execute migration toolkit

Initiates the toolkit without starting the service

`sudo python3 Main.py` 

TODO: Implement "all files by default" argument using argparse

### Executes migration toolkit and initiates Rest API service

`sudo sh run.sh` 

#### Alternate database 

must be configured in the `Proto/api/protoapi/settings/dev.py` file by modifying the `DATABASES` variable

## Access via Rest API endpoint

`curl -X 'GET' 'http://127.0.0.1:8000/protoapi/record'`

`-H 'accept: application/vnd.api+json'`

### Filters

`/protoapi/record?filter[timestamp]={TIMESTAMP}&filter[user_iduser]={IDUSER}'`