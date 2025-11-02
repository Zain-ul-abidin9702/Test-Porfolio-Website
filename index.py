print("This is my portfolio website")
print("Nice test")


users = []

def printUsers():
    print("Print users : ",users);

def getAllUsers():
    return users

def createUser(user):
    users.append(user)

print("Creating User");
createUser({"name":"zain","age":22})

printUsers();
print("Get All Users : ",getAllUsers());

print("Creating User");
createUser({"name":"ehsan","age":45})