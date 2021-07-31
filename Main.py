import os
import inquirer
import argparse
import struct
import urllib.request
import json
import django 
from django.conf import settings
from django.db.models import Sum

from api.protoapi.settings.dev import DATABASES
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=["api.protoapi",])
django.setup()

from api.protoapi.models import Record,Type,User

# ---- Global variables ----
path = os.path.dirname(os.path.abspath(__file__))
headers = { 'accept' : 'application/vnd.api+json',
            'Content-Type' : 'application/vnd.api+json' }#TODO: Include AuthBearer header when IsAuthenticated is active.
host    = "http://localhost:8000"

# ---- Files ----
filesList = []
for file in os.listdir(f"{path}"):
    if (file.endswith(".dat")):
        filesList.append(f"{path}\{file}")

questions = [
            inquirer.Checkbox(
                'file',
                message="Which file(s)?",
                choices=filesList,
            ),
            ]
answers = inquirer.prompt(questions)

recordList:Record = []
for answer in answers['file']:
    print(f"Selected File: {answer}")
    try:
        # -- Header --
        file = open(answer, "rb")
        magicString = file.read(4) 
        print(f"Magic String: {magicString}")

        version = int.from_bytes(file.read(1), byteorder='big', signed=False)
        print(f"Version: {version}")

        records = int.from_bytes(file.read(4), byteorder='big', signed=False) 
        print(f"Header defined Length: {records}") 

        #-- Record--
        for i in list(range(records)):
            typeByte = file.read(1)
            type        = int.from_bytes(  
                            typeByte,
                            byteorder='big', 
                            signed=False)
            timestamp   = int.from_bytes(   
                            file.read(4),
                            byteorder='big', 
                            signed=False)
            user_iduser = int.from_bytes(   
                            file.read(8),
                            byteorder='big', 
                            signed=False)
            ammount     = None
            if(Type.hasField(typeByte)):
                ammount = struct.unpack('!d', file.read(8))[0]

            r = Record  (   None,
                            type_idtype = Type(idtype=type, name=Type.getTypeName(typeByte)),
                            timestamp   = timestamp,
                            user_iduser = User(iduser=user_iduser),
                            ammount     = ammount
                        ) 
            recordList.append(r)
            print(f"Record {i}/{records}: {r.type_idtype.name:14} | {r.timestamp:12} | {r.user_iduser.iduser:22} | {r.ammount}")

            r.user_iduser.save()
            r.type_idtype.save()#TODO: Implement default inserts on django migration.

            # Validate existing record and test JSON REST Endpoint 
            url = f"{host}/protoapi/record?filter[timestamp]={r.timestamp}&filter[user_iduser]={r.user_iduser.iduser}"
            req = urllib.request.Request(url, headers=headers)
            data = json.loads(urllib.request.urlopen(req).read())
            
            if(len(data['data']) != 0):
                print(f"Record {i}: exists in db {len(data['data'])} times")
            else:
                r.save()

            
        file.close()
        print(f"Finished execution of: {answer}")
    except Exception as e:
        print(f"Exception: {str(e)} ")


print(f"Finished execution.")
print(f"total credit amount={Record.objects.filter(type_idtype=1).aggregate(Sum('ammount'))['ammount__sum']}")
print(f"total debit amount={Record.objects.filter(type_idtype=0).aggregate(Sum('ammount'))['ammount__sum']}")
print(f"autopays started={Record.objects.filter(type_idtype=2).count()}")
print(f"autopays ended={Record.objects.filter(type_idtype=3).count()}")


thisUser = 2456938384156277127
debit =   Record.objects.filter(    user_iduser=thisUser, 
                                    type_idtype=0
                                ).aggregate(Sum('ammount'))['ammount__sum']
if debit is None: debit = 0.0

credit = Record.objects.filter(     user_iduser=thisUser, 
                                    type_idtype=1
                                ).aggregate(Sum('ammount'))['ammount__sum']
if credit is None: credit = 0.0


print(f"balance for user {thisUser}={float(credit)-float(debit)}")