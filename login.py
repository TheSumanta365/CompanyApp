def login(username, password):
    if username.lower() == "admin" and password == "admin123":
        print("Login Successful")
    else:
        print("Invalid Credentials")

