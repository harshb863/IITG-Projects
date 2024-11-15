import csv
import hashlib
import uuid
class UserManagement:
    def startUp(self):
        print("User Management System")
        print("1. New User")
        print("2. Existing User")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        return choice
    
    def newUser(self):
        print("New User")
        while True:
            username = input("Enter your username: ")
            if self.checkUser(username, "", "userExists"):
                print("User already exists")
                continue
            else:
                break
        password = input("Enter your password: ")
        return username, password
    
    def saveUser(self, username, password):
        if username == "" or password == "":
            print("Invalid Data")
            return
        with open("C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/User Management/users.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print("User created successfully")

    def checkUser(self, username, password, process):
        with open("C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/User Management/users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if not ''.join(row):
                    return False
                elif process == "userExists":
                    if row[0] == username:
                        return True
                elif process == "login":   
                    if row[0] == username and row[1] == password:
                        print("Login Successful")
                        return True
    
    def hashPassword(self, password):
        salt = "5gz"
        dataBase_password = password+salt
        hashed = hashlib.md5(dataBase_password.encode())
        return hashed.hexdigest()
    
    def menu(self):
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Completed")
        print("4. Delete a Task")
        print("5. Logout")
        choice = int(input("Enter your choice: "))
        return choice
    
    def addTask(self, username):
        index = 0
        if username == "":
            print("Invalid User")
            return
        task = input("Enter the task: ")
        with open("C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/User Management/tasks.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([username,uuid.uuid1(),task, "Pending"])
        print("Task added successfully")
    
    def viewTasks(self, username):
        with open("C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/User Management/tasks.csv", "r") as file:
            reader = csv.reader(file)
            print("Task\t\t\tStatus")
            for row in reader:
                if not ''.join(row):
                    continue
                if row[0] == username:
                    print(row[2],"\t\t\t",row[3])
    
    def markComplete(self, username):
        task = input("Enter the task to mark as complete: ")
        with open("C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/User Management/tasks.csv", "r") as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                if not ''.join(row):
                    continue
                if row[0] == username and row[2] == task:
                    row[3] = "Completed"
                data.append(row)
        with open("C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/User Management/tasks.csv", "w") as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)    
    
    def deleteTask(self, username):
        task = input("Enter the task to delete: ")
        with open("C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/User Management/tasks.csv", "r") as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                if not ''.join(row):
                    continue
                if row[0] == username and row[2] == task:
                    continue
                data.append(row)
        with open("C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/User Management/tasks.csv", "w") as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)