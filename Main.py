from Models import Record,Type
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
    # logger.debug(f"Loading URL's From: {answer}")
    print(f"Selected File: {answer}")
    try:
        # -- Header --
        file = open(answer, "rb")
        magicString = file.read(4) 
        print(f"Magic String: {magicString}")

        version = int.from_bytes(  file.read(1) , 
                                byteorder='big', 
                                signed=False)
        print(f"Version: {version}")

        records = int.from_bytes(file.read(4), 
                                byteorder='big', 
                                signed=False) 
        print(f"Header defined Length: {records}") 

        #-- Record--
        for i in list(range(records)):

            typeByte = file.read(1)
            # type = Type.getType(typeByte)
            # print(f"Type: {type}")

            timestamp = file.read(4)
            # timestamp = int.from_bytes( file.read(4), 
            #                             byteorder='big', 
            #                             signed=False)
            # print(f"Timestamp: {timestamp}")

            userID = file.read(8)
            # userID = int.from_bytes(file.read(8), 
            #                         byteorder='big', 
            #                         signed=False)
            # print(f"userID: {userID}")
           
            # line = f"{type:14} | {timestamp:12} | {userID:22}"
            ammount = None
            if(Type.hasField(typeByte)):
                ammount = struct.unpack('!d', file.read(8))[0]
                # print(f"amount in dollars={ammount}")
                # line = f"{line} | {ammount:}"

            r = Record  (   None,
                            typeByte,
                            timestamp,
                            userID,
                            ammount
                        )
            recordList.append(r)

            line = f"{r.type_idtype.name:14} | {r.timestamp:12} | {r.user_iduser.iduser:22} | {r.ammount}"
            print(f"{line}")

        file.close()
    except Exception as e:
        print(f"Exception: {str(e)} ")

# print(f"total credit amount={byte}")
# print(f"total debit amount={byte}")
# print(f"autopays started={byte}")
# print(f"autopays ended={byte}")
# print(f"balance for user {byte}={byte}")