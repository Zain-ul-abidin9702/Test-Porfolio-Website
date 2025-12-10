
users = []

def printUsers():
    print("Print users : ",users);

def getAllUsers():
    return users

def createUser(user):
    users.append(user)

def getUser(name):
    for user in users:
        
        if user["name"]== name:
            return user
        
    return None


createUser({"name":"zain","age":22})
printUsers();


createUser({"name":"ehsan","age":45})
printUsers()

user = getUser("ahmed")
print("User : ",user);