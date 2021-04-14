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
else:
    print("Login unsuccessful")
    print("\n")
    exit()

file = open("pwdatabase.txt", "w+")

## Funtional Requirement 4: Store up to 10 credential records.
i = 1
while i <=2  :
    print("Enter the following server #", i, " information to store: ")
    server = input("Enter Server Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    ## Functional Requirements 1 & 2: store server name, username, & password...
    ## ... on password database.
    file.write(server + "\n")
    file.write(username + "\n")
    file.write(password + "\n")
    print("The following credentials were stored in the pwdatabase.txt file: \n",
    "Server Name:" + server + "\n", "Username: " + username + "\n",
    "Password: " + password + "\n")

    i += 1

print("CREDENTIAL CAPACITY REACHED!!!")
file.close()

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
        dataAdd = input("Enter what you would like to add: ")
        reader.write(dataAdd)
        print("New data added to pwdatabase.txt: " + dataAdd + "\n")

    elif edit == "delete":
        dataDelete = input("Enter what you would like to delete: ")
        for dd in lines:
            if dd.strip("\n") != dataDelete:
                reader.write(dd)

    elif edit == "update":
        dataOld = input("Enter the old credential you would like to update: ")
        dataReplace = input("Enter the new updated credential: ")
        for du in lines:
            # if du.strip("\n") == dataOld:
            reader.write(du.replace(dataOld, dataReplace))

reader.close()
