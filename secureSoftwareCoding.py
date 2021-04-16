"""
ISA 320
secureSoftwareCoding.py
Read the "README + ISA 320 + Daryl Madela Jr" text file
for how to compile and run this Python 3 code.
Python 3 program that fulfills Functional Requirements 1 to 5
and Security Requirement 1 to 2.
By Daryl Madela Jr
"""

## Security Requirement 1: enter username and password to access credentials
print("Enter in given username & password to access password database: ")
un = input("Enter given username: ")
pw = input("Enter given password: ")
if un == "isa" and pw == "320":
    print("Login sucessful")
    print("\n")
else:
    print("Login unsuccessful")
    print("\n")
    exit()

file = open("pwdatabase.txt", "w")

## Funtional Requirement 4: Store up to 2 credential records.
i = 1
while i <=2 :

    print("Enter the following server #", i, " information to store: ")
    server = input("Enter Server Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    print("\n")

    file.write(server + "\n")
    file.write(username + "\n")
    file.write(password + "\n")

    # enterList = []
    # with open("pwdatabase.txt", "r+") as reader:
    #     for line in reader.readlines():
    #         removeSpace = line.replace("\n","")
    #         enterList.append(removeSpace)
    # reader.close()
    
    # if server in enterList:
    #     print("Sorry, server name used already.")
     
    i += 1
file.close()

print("CREDENTIAL CAPACITY REACHED!!!")
print("\n")


with open ("pwdatabase.txt", "r") as reader:
    lines = reader.readlines()
reader.close()

j = 0
## Functional Requirement 3: retrieve the username and password by inputting servername 
server = input("Enter Server Name for login credentials: ")
if server.lower() == server:
    print(lines[j + 1])
    print(lines[j + 2])

serverList = []
with open("pwdatabase.txt", "r+") as reader:
    for line in reader.readlines():
        removeSpace = line.replace("\n","")
        serverList.append(removeSpace)
reader.close()
print("Current server list credentials: ")
print(serverList)
print("\n")

## Functional Requirement 5: add, update, or delete specific credentials
print("What function would you like to do?")
edit = input("Type 'add', 'update', or 'delete' to select function: ")

with open ("pwdatabase.txt", "a+") as reader:
    reader.seek(0)
    lines = reader.readlines()
    if edit == "add":
        dataAdd = input("Enter a credential you would like to add: ")
        reader.write(dataAdd)
        print("New credential added to pwdatabase.txt: " + dataAdd + "\n")

    elif edit == "delete":
        dataDelete = input("Enter the credential you would like to delete: ")
        for dd in lines:
            if dd.strip("\n") != dataDelete:
                reader.write(dd)
        print("Old credential deleted from pwdatabase.txt \n")

    elif edit == "update":
        dataOld = input("Enter the old credential you would like to update: ")
        dataReplace = input("Enter the new updated credential: ")
        for du in lines:
            reader.write(du.replace(dataOld, dataReplace))
        print("Old credential updated to pwdatabase.txt \n")

reader.close()
