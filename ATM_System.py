import sys
from typing import Self
def exit_program():
    print("Exiting the program...")
    sys.exit(0)
class cardHolder():
    def __init__(self,cardNum,pin,firstName,lastName,balance):
        self.cardNum = cardNum 
        self.pin = pin
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance

    ## Get method
    def get_cardNum(self):
        return self.cardNum
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_balance(self):
        return self.balance
    def get_pin(self):
        return self.pin
    
    #set method
    def set_cardNum(self,newValue):
        self.cardNum = newValue
    def set_firstName(self,newValue):
        self.firstName = newValue
    def set_lastName(self,newValue):
        self.lastName = newValue
    def set_pin(self,newValue):
        self.pin = newValue
    def set_balance(self,newValue):
        self.balance = newValue
    
    #print method
    def print_out(self):
        print ("Card : ",self.cardNum)
        print ("pin : ",self.pin)
        print ("balance : ",self.balance)
        print ("firstName : ",self.firstName)
        print ("lastName : ",self.lastName)

##########################
def print_menu(self): #to print menu
    print ("Please Enter your choose ....")
    print ("1. Deposit")
    print ("2. Withdraw")
    print ("3. Show Balance")
    print ("4. Exit")

def deposit(cardHolder): #to deposit
    try:
        deposit = float(input("Enter How much u want to deposit : "))
        cardHolder.set_balance(cardHolder.get_balance()+deposit)
        print ("your deposit with  : ",deposit," is successfully and your new balance is : ",cardHolder.get_balance())
    except :
        print("Invalid input")

def withdraw(cardHolder): #to withdraw
    try:
        withdraw = float(input("Enter How much u want to withdraw : "))
        #to check if user have enough money
        try:
            if(cardHolder.get_balance() >= withdraw):
                cardHolder.set_balance(cardHolder.get_balance()-withdraw)
                print ("your withdraw with : ",withdraw," is successfully and your new balance is : ",cardHolder.get_balance())
            else:
                print("u dont have enough money")    
        except :
            print("Invalid input")        
    except:
        print("Invalid input")    

def check_balance(cardHolder):#to show balance
    print("Your current balance is : ",cardHolder.get_balance())
####################
current_user = cardHolder("","","","","")

# list of users
list_of_cardHolders =[]
list_of_cardHolders.append(cardHolder("45634674545636546",3465,"omar","khalifa",3456.33))
list_of_cardHolders.append(cardHolder("45634346453636546",2634,"ahmed","mos3ad",5674.353))
list_of_cardHolders.append(cardHolder("45784534545636546",8456,"mohamed","jom",563.45))
list_of_cardHolders.append(cardHolder("45634674545745632",7453,"saad","kajgf",5234.335))
list_of_cardHolders.append(cardHolder("95675454545636546",7744,"tamed","mosssa",3325.443))

#check card number
debitCardNumber =""
while True:
    try:
        debitCardNumber =input("please insert your debit Card Number : ")
        debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum ==debitCardNumber]
        if(len(debitMatch)>0):
            current_user = debitMatch[0]
            break
        else:
            print("Card number not recognized 1. Please try again.")  
    except :
        print("Card number not recognized 2. Please try again.")

#check pin number    
pinCounter =0
while True:
    
        userPin = int(input("Please enter your PIN : ").strip())
        if(current_user.get_pin() == userPin):
            break
        else:
            pinCounter += 1
            if(pinCounter == 3):
                exit_program(1)
            else:    
                print("wrong pin Please try again u have ",3-pinCounter, "trys!")

    


# wlecome page
print("Welcome ",current_user.get_firstName(), " : ")
option =0
while True:
    print_menu(Self)
    try:
        option = int(input())
    except:
        print("Invalid input. Please try again")    
    if(option == 1 ):
        deposit(current_user)
    elif(option ==2):
        withdraw(current_user)   
    elif(option ==3):
        check_balance(current_user)
    elif(option ==4):
        break      
    else:
        print("Invalid option. Please try again") 
        option=0  
print("Thank you.......")