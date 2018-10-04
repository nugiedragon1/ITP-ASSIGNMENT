#empty space for memory in the bank
acc=[]
bal=[]
#for object bank
class bank:
    #register function for the customer account
    def register(self):
        global p
        firstName = input("Enter your First Name :")
        lastName = input("Enter your Last name :")
        p = customer(firstName,lastName)
        p.customerName()
#for Object customer
class customer():
    #recognize the customer with first name and last name
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        #for the registered customer's account with name
    def customerName(self):
        global acc
        global bal
        bal.append(0)
        acc.append(self.firstName+ " "+self.lastName)
        print('\n Your account successfuly active\n')
        #deposit function
    def deposit(self):
        enteracc=int(input("Enter your account number : "))
        enterdep=int(input("Amount of money :"))
        bal[enteracc] += enterdep
        for x in range(len(acc)):
            print("\n Acount Number : ", x , "\n customer:" , acc[x], "\n Balance : Rp." , bal[x], "\n")

    def withdraw(self):
        global bal
        enteracc= int(input("Enter your account number :"))
        enteramount = int(input("Amount of money :"))
        bal[enteracc] -= enteramount
        for x in range (len(acc)):
            print ("\n Account Number :", x , '\n customer:', acc[x], "\n Balance : Rp.", bal[x], "\n")

    def checkbalance(self):
        global acc
        global bal
        enteracc = int(input("Enter your account number :"))
        print("\n Account Number :", enteracc, "\n customer :", acc[enteracc], "\n balance : Rp.", bal[enteracc], "\n")
#for all the commands in the ATM
command = 1
while command!=0 :
    print("Welcome To Life\n")
    print("Select a transaction\n")
    print("0.Quit")
    print("1.Register")
    print("2.Information")
    print("3.Deposit")
    print("4.Withdraw")
    print("5.Balance Information\n")
    command=int(input("Select the transaction :"))
    #THE COMMANDS IN THE ATM MACHINE TO DECIDE ANY TRANSACTION
    if command ==1 :
        b = bank()
        b.register()
    elif command ==2:
        for x in range (len(acc)):
            print ("\n Account Number:",x,"\n customer:",x,"\n balance : Rp.", bal[x],"\n")
    elif command==3:
        p.deposit()
    elif command ==4 :
        p.withdraw()
    elif command==5:
        p.checkbalance()
    elif command==0:
        print ("See You Next Time")
    else :
        print ("Command Unknown")

