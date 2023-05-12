import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "BOotWw40!",
    database = "Bank database"
)
mycursor = db.cursor()
mycursor.execute("SELECT * FROM account")
accounts_list = []
for x in mycursor:
    accounts_list.append(x)

class bank_user:
    def __init__(self, number, pin, name, balance):
        self.number = number
        self.pin = pin
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Your balance is " + str(self.balance))

    def deposit_money(self):
        amount = int(input("How much money do you want to deposit?"))
        self.balance += amount
        print("Your new balance is " + str(self.balance))

    def withdraw_money(self):
        withdraw = int(input("How much money would you like to withdraw?"))
        self.balance -= withdraw
        print("Your new balance is " + str(self.balance))

def home_screen():
    print("Welcome to Honesty Banks!")
    choice = input("what would you like to do? a. Log in  b. Create an account  c. Exit")
    if choice == "a":
        num = int(input("Enter your account number"))
        if num in accounts_list:
            mycursor.execute("SELECT pin FROM accounts WHERE number = num")
            acct_pin = int(input("Enter the pin"))
            for x in mycursor:
                if x == acct_pin:
                    mycursor.execute("SELECT name FROM accounts WHERE pin = acct_pin")
                    name
                    for x in mycursor:
                      name = x  
                      print("Welcome, " + x)
                      return x
    if choice == "b":
        nm = input("Enter your name ")
        num = input("Choose an account number")
        acct_pin = ("Create a 6 number pin please")
        mycursor.execute("INSERT INTO account(number, pin, name, balance) VALUES(num, acct_pin, nm, 0)")
        new = bank_user(num, acct_pin, nm, 0)
        return nm
    if choice == "c":
        print("Goodbye!")
        return 'c'

def logged_in_screen():
    nm = home_screen()
    choice = input("What would you like to do?  a. Check balance  b. Deposit money  c. Withdraw money  d. Exit")
    if choice == 'a':
        mycursor.execute("SELECT balance FROM account WHERE name = nm")
        for x in mycursor:
            print(x)
    if choice == 'b':
        depo = int(input("What is your deposit?"))
        mycursor.execute("SELECT balance FROM account WHERE name = nm")
        for x in mycursor:
            x += depo
            print(x)
    if choice == 'c':
        withd = int(input("What is your withdrawl?"))
        mycursor.execute("SELECT balance FROM account WHERE name = nm")
        for x in mycursor:
            x -= with
            print(x)
    if choice == 'd':
        print("Goodbye!")
        
def run():
    val = home_screen()
    if val != 'c':
        logged_in_screen
