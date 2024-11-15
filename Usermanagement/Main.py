from Logic import UserManagement
def main():
    ref = UserManagement()
    while True:
        selection = ref.startUp()
        if selection == 1:
            username, password = ref.newUser()
            ref.saveUser(username, ref.hashPassword(password))
        elif selection == 2:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if ref.checkUser(username, ref.hashPassword(password), "login"):
                while True:
                    choice = ref.menu()
                    if choice == 5:
                        break
                    elif choice == 1:
                        ref.addTask(username)
                    elif choice == 2:
                        ref.viewTasks(username)
                    elif choice == 3:
                        ref.markComplete(username)
                    elif choice == 4:
                        ref.deleteTask(username)
            else:
                print("Login Failed")
        elif selection == 3:
            exit()

if __name__ == "__main__":
    main()
