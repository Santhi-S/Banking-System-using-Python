import random
import string

account_details = {
    'Akhil': {'pwd': 1010, 'balance': 40000},
    'Anila': {'pwd': 2300, 'balance': 23000},
    'Rose': {'pwd': 4900, 'balance': 10000},
    'Shreya': {'pwd': 5090, 'balance': 20000},
    'Tina' : {'pwd': 2001, 'balance': 20000}
}

def register():
    input_name = input("Enter new user name: ")
    if (input_name not in account_details):
        new_account_details = {}
        new_account_details['pwd'] = int(input("Enter new password: "))
        new_account_details['balance'] = float(input("Enter opening balance: "))
        account_details[input_name] = new_account_details
        print("Account created successfully")
        print("Please login to continue")
        login()
    else:
        print("User already exists. Please enter another user name or login if you have already registered")

def login():
    global input_name
    input_name = input("Enter the username: ")
    input_pwd = int(input("Enter the password: "))
    if (input_name in account_details):
        stored_pwd = account_details[input_name]['pwd']
        if (input_pwd == stored_pwd):
            res = captcha()
            print(res)
            input_captcha = input("Enter the above captcha: ")
            if (input_captcha == res):
                print("Login successful")
                features()
            else:
                print("Incorrect captcha. Please try again")
                login()
        else:
            print("Incorrect password. Please try again")
            login()
    else:
        print("User name not found. Please try again")

def deposit(input_name):
    deposit_amount = float(input("Enter the amount to be deposited: "))
    if (deposit_amount > 0):
        account_details[input_name]['balance'] += deposit_amount
        print("Deposit successful\nYour balance is",account_details[input_name]['balance'])
    else:
        print("Deposit failed. Please enter valid deposit amount")
    options()
def withdraw(input_name):
    withdraw_amount = float(input("Enter the amount to be withdrawn: "))
    if (withdraw_amount <= account_details[input_name]['balance'] and withdraw_amount >0 ):
        account_details[input_name]['balance'] -= withdraw_amount
        print("Withdrawal successful")
        print("Your current balance is",account_details[input_name]['balance'])
    elif (withdraw_amount < 1):
        print("Withdrawal failed\nPlease enter valid withdrawal amount")
    else:
        print("Insufficient fund in your account")
    options()

def transfer(input_name):
    print("----- Welcome to fund transfer -----")
    beneficiary_name = input("Enter beneficiary name: ")
    transfer_amount =  float(input("Enter amount to transfer: "))
    if (transfer_amount <= account_details[input_name]['balance'] and transfer_amount > 0) :
         if (beneficiary_name in account_details):
            account_details[beneficiary_name]['balance'] += transfer_amount
            account_details[input_name]['balance'] -= transfer_amount
            print("Fund transfer successful to",beneficiary_name)
            print("Your current balance is:",account_details[input_name]['balance'])

         else:
            print("Invalid beneficiary\nPlease enter valid beneficiary")
            transfer(input_name)
    elif (transfer_amount < 1):
        print("Enter valid amount")
    else:
        print("Insufficient fund in your account")
    options()
def captcha():
    length = 6
    captcha_characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(captcha_characters) for i in range(length))
    return captcha

def options():
    print("Please select from the options")
    print("1. Continue to banking operations")
    print("2. Exit from MyBank")
    choice = input("Please enter an option: ")
    if choice == '1':
        features()
    elif choice == '2':
        print("----- Thank you for using MyBank financial services -----")
    else:
        print("Invalid option. Try again")
        options()
def features():
    print("How can I help you?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Fund transfer")
    print("4. Current balance")
    print("5. Exit from MyBank")
    option = input("Please enter an option: ")
    if option == '1':
        deposit(input_name)
    elif option == '2':
        withdraw(input_name)
    elif option == '3':
        transfer(input_name)
    elif option == '4':
        current_balance()
    elif option == '5':
        print("----- Thank you for using MyBank financial services -----")
    else:
        print("Invalid option selected")
        features()
def current_balance():
    print("Your current balance is:",account_details[input_name]['balance'])
    options()


print("----- Welcome to MyBank financial services -----")
print("1. Register new user")
print("2. Login")
print("3. Exit")
option = input("Please enter an option: ")
if option == '1':
    register()
elif option == '2':
    login()
elif option == '3':
    print("----- Thank you for using MyBank financial services -----")
else:
    print("You have selected invalid option. Please select 1,2 or 3")





