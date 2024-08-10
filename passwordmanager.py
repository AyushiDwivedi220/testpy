master_password= input("Enter your master password to acess password manager: ")

if master_password == "321":
    def add():
        name=input("Enter your account name: ")
        password=input("Enter your password: ")
        with open ("password.txt","a") as f:
            f.write(name + "|" + password)


    def view():
        with open("password.txt","r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:",user," Password: ",passw)

    while True:
        mode = input("Do you wanna add password,view list or quit:")
        if mode == "quit":
            quit()

        if mode == "add":
            add()
        elif mode == "view":
            view()
        else:
            print("Invalid input..")

else:
    print("YOU ENTERED THE INCORRECT MASTER PASSWORD ")