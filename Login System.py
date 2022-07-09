import hashlib
def signup():
    email=input("Enter Email ID")
    pwd=input("Enter Password")
    conf_pwd=input("Confirm Password")

    if(conf_pwd==pwd):
        enc=conf_pwd.encode()
        hash1=hashlib.md5(enc).hexdigest()
        with open("credentials.txt","w") as f:
            f.write(email+"\n")
            f.write(hash1)
        f.close()
        print("You have registered successfully! \n")
    else:
        print("Password is not same as above \n")  




def signin():
    email=input("Enter Email ID")
    pwd=input("Enter Password")

    auth=pwd.encode()
    auth_hash=hashlib.md5(auth).hexdigest()
    with open("credentials.txt","r") as f:
        stored_email,stored_pwd=f.read().split("\n")
    f.close()

    if(email==stored_email and stored_pwd==auth_hash):
        print("Logged in Successfully \n")
    else:
        print("Login Failed! \n")

while 1:
    print("******Login System******")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        signin()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")