import datetime
import csv
from Format import green, format_date
import warnings
class MyExpense:
    loaded_expense = []
    def __init__(self):
        self.loaded_expense = []

    def welcome(self):
        print(f"🎯Running Personal Expense Tracker App")
        print(f"Hello Sir, how can i help you, please select an option below")
        arr = ["Add expense", "View expenses", 'Track budget', 'Save expenses', 'Exit']
        for i, option_name in enumerate(arr):
            print(f"Press Button {i+1} for Option '{green(option_name)}'")
        selected_index = int(input(f"Press button: "))
        if selected_index == 1:
            self.add()
        elif selected_index == 2:
            self.view()
        elif selected_index == 3:
            self.track()
        elif selected_index == 4:
            self.save()
        else:
            self.save()
            exit()
        user_input = input(f"is there anything else you would like to do? (yes/no)")
        if user_input.lower() == 'yes' or user_input.lower() == 'y':
            pass
        else:
            self.save()
            exit()
    
    def setBudget(self):
        f = open('C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/Expense Tracker/budget.txt', 'w')
        f.write(input(f"Please enter your budget"))
        print(f"Budget set successfully")
        
    
    def track(self):
        print(f"Please select an option below")
        arr = ["Set Budget", "View Budget"]
        for i, option_name in enumerate(arr):
            print(f"Press Button {i+5} for Option '{green(option_name)}'")
        selected_index = int(input(f"Press button: "))
        if selected_index == 5:
            self.setBudget()
        elif selected_index == 6:
            self.showNotification()
    
    def showNotification(self):
        with open('C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/Expense Tracker/budget.txt', 'r') as file:
            budget = file.read()
        total_expense = 0
        with open('C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/Expense Tracker/expense.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not ''.join(row):
                    continue
                total_expense += int(row[2])
        for i in self.loaded_expense:
            total_expense += int(i['Amount'])
        if total_expense > int(budget):
            # print(f"Your expenses have exceeded the budget")
            warnings.warn("Your expenses have exceeded the budget")
        else:
            print(f"Your expenses are within the budget, your available budget is {int(budget) - total_expense}")
    
    def save(self):
        with open('C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/Expense Tracker/expense.csv', 'a') as file:
            writer = csv.writer(file)
            if len(self.loaded_expense) == 0:
                return
            for i in self.loaded_expense:
                writer.writerow([i['Date'], i['Category'], i['Amount'], i['Description']])
    
    def view(self):
        with open('C:/Users/bajpaih/Downloads/IIT-G Projects/IIT-G Projects/Expense Tracker/expense.csv', 'r') as file:
            reader = csv.reader(file)
            print(f"Date\t\t\tCategory\t\t\t\tAmount\t\t\tDescription")
            # print(reader)
            for row in reader:
                if not ''.join(row):
                    continue
                if len(row[0]) == 0 or row[1] == 0 or row[2] == 0 or row[3] == 0:
                    print(f"Data is incomplete")
                    continue
                print(f"{format_date(row[0])}\t\t{row[1]}\t\t\t\t\t{row[2]}\t\t\t{row[3]}")
        for i in self.loaded_expense:
            print(f"{format_date(i['Date'])}\t\t{i['Category']}\t\t{i['Amount']}\t\t{i['Description']}")

    def add(self):
        expense_dict1 = {}
        full_date = datetime.datetime.now()
        print(f"Please Provide your transaction details below")
        while True:
            input_date = input(f"Please Enter you date of transaction in YYYY-MM-DD Format :" )
            lv_date_split = input_date.split("-")
            if len(lv_date_split[0]) == 4 and lv_date_split[0].isnumeric():
                expense_dict1["Date"] = input_date
                break
            else:
                print(f"Please enter the date in correct format")
                continue
        while True:
            expense_dict1["Category"] = input(f"Please provide expense category")
            if expense_dict1["Category"].isalpha():
                break
            else:
                print(f"Please enter the correct category")
                continue
        while True:
            input_expense = input(f"Please enter the expense amount")
            if input_expense.replace(".","").isnumeric():
                expense_dict1["Amount"] = input_expense
                break
            else:
                print(f"Please enter the correct amount")
                continue
        expense_dict1["Description"] = input(f"Please enter the description of your expense")
        
        expense_dict1["Timelog"] = datetime.datetime.now()
        if len(expense_dict1["Date"]) != 0 and len(expense_dict1["Category"]) != 0 and len(expense_dict1["Amount"]) != 0 and len(expense_dict1["Description"]) != 0:
            self.loaded_expense.append(expense_dict1)
            print(f"Transaction added successfully")