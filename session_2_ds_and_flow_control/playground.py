
# break and Continue

# print login success if we have proper username and password



while True :
    user = input("Enter Username : ")
    password = input("Enter Password : ")
    if user == 'admin' and password == 'admin' :
        print("Login Success")
        break
    else:
        print("Invalid Credentials, Username or Password Incorrect")
