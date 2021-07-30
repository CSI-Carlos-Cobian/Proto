import os
import inquirer
import Types
import argparse


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

for answer in answers['file']:
    # logger.debug(f"Loading URL's From: {answer}")
    print(f"Selected File: {answer}")
     # try{
# -- Header --
print(f"Header: {str()}")
magicstring ="MPS7"
print(f"String: {str.encode(magicstring)}")
b : bytes = bytes(magicstring, encoding="raw_unicode_escape")
print(f"String: {b}")
print(f"Version: {str()}")
print(f"Header defined Length: {str()}") 
print(f"total credit amount={str()}")

# for(Header defined Length): #TODO
   
#-- Record--
type = Types.getType(b'\x00')
print(f"Type: {type}")
print(f"Timestamp: {str()}")
print(f"userID: {str()}")

print(f"total credit amount={str()}")
print(f"total debit amount={str()}")
print(f"autopays started={str()}")
print(f"autopays ended={str()}")
print(f"balance for user {str()}={str()}")
    # }catch InvalidDataException as e {}