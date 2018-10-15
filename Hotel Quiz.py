str(input("Check in?")) #CHECK IN QUESTION
class HotelProg() :     #CLASS FOR HOTEL PROGRAM
    def __init__ (self,type):
        self.pricePresident = 2000000
        self.priceSuite = 1500000
        self.priceSack = 1000000
        self.presidentList = []
        self.suiteList = []
        self.sackList = []
        self.type= type
    def checkRoom(self):        #CLASS FOR EACH CATEGORY OF ROOM
        print("President\t\tSuite\t\tSack")
        presidentAvbl = int(len(self.presidentList))
        suiteAvbl = int(len(self.suiteList))
        sackAvbl = int(len(self.sackList))
        print("",presidentAvbl,"\t\t",suiteAvbl,"\t\t",sackAvbl)
    def Revenue(self):      #REVENUE FOR ALL ROOMS
        if int(len(self.presidentList)) == 0 and int(len(self.suiteList)) == 0 and int(len(self.sackList))== 0:
            print ("total revenue :"," Rp.0")
        else :
            presidentAvbl = int(len(self.presidentList))
            suiteAvbl = int(len(self.suiteList))
            sackAvbl = int(len(self.sackList))
            revenue = presidentAvbl *self.pricePresident + suiteAvbl * self.priceSuite + sackAvbl *self.priceSack
            print("\nTotal Revenue : " ,"RP", revenue, "\n")
class Category(HotelProg):      #CLASS FOR EACH ROOM
    def presidentRoom(self):
        self.presidentList.append(self.type)
        print("\nPrice : ",self.pricePresident,"\n")
    def suiteRoom(self):
        self.suiteList.append(self.type)
        print("\nPrice : ", self.priceSuite,"\n")
    def sackRoom(self):
        self.sackList.append(self,type)
        print("\nPrice : ",self.priceSack,"\n")
x = Category("Category")
while True :                # CHOICES IN THE CHECK IN OPTIONS
    print("Category of Rooms : ")
    print("1. \tPresident Room\t\t")
    print("2. \tSuite Room\t\t")
    print("3. \tSack Room\t\t")
    print("4. \t Check Data")
    print("5. \tRevenue")
    print("6. \tClose")
    choice =int(input("Enter Command : "))      #ITS ALL FOR THE COMMAND
    if choice ==1 :
        x.presidentRoom()
    if choice == 2 :
        x.suiteRoom()
    if choice == 3 :
        x.sackRoom()
    if choice == 4 :
        x.checkRoom()
    if choice == 5 :
        x.Revenue()
    if choice == 6 :
        print("See ya Later")
        break

# I THINK THIS IS MY LIMIT FOR TODAY I CANT EVEN THINK ANYTHING ELSE




