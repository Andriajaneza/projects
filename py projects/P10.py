print("Register")

name = (input("name : "))
surname = (input("namsurname : "))
nickname = (input("nickname : "))
email = (input("email : "))
password = (input("password : "))

print("")
print("hello " + name)
print("")

print("login")
print("")

emailX = (input("email : "))
passwordX = (input("password : "))
if emailX == email and passwordX == password:
    print("you logged in")
if emailX is not email or passwordX is not password:
    print("nope")
    