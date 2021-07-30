from models import Record,Type
import os
import inquirer
import argparse
import struct

path = os.path.dirname(os.path.abspath(__file__))

# == Links ==
linksList = []
for file in os.listdir(f"{path}"):
    if (file.endswith(".dat")):
        linksList.append(f"{path}\{file}")

questions = [
            inquirer.Checkbox(
                'file',
                message="Which file(s)?",
                choices=linksList,
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
            timestamp = file.read(4)
            userID = file.read(8)
            ammount = None
            if(Type.hasField(typeByte)):
                ammount = struct.unpack('!d', file.read(8))[0]

            r = Record  (   None,
                            typeByte,
                            timestamp,
                            userID,
                            ammount
                        )
            recordList.append(r)

            print(f"{r.type_idtype.name:14} | {r.timestamp:12} | {r.user_iduser.iduser:22} | {r.ammount}")

        file.close()
    except Exception as e:
        print(f"Exception: {str(e)} ")

# print(f"total credit amount={byte}")
# print(f"total debit amount={byte}")
# print(f"autopays started={byte}")
# print(f"autopays ended={byte}")
# print(f"balance for user {byte}={byte}")