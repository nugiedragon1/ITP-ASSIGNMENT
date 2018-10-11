print("=================================================\n",
 "\tToll Payment Systems \n" ,"\tPt.Jasa Marga,Tbk\n","===============================================")        #Print the header of Toll
class TollGate():
    def __init__(self,type):
        self.priceCar = 6000
        self.priceBus = 8000
        self.priceTruck = 10000
        self.busList = []
        self.carList = []
        self.truckList = []
        self.type = type
    def checkData(self):                    #ITS ALL FOR CHECK ALL THE VEHICLE THAT COME THROUGH THE GATE AND PUT IT INTO A LIST
        print("---------------------")
        print("Car\t\tBus\t\tTruck")
        print("---------------------")
        carCou = int(len(self.carList))
        busCou = int(len(self.busList))
        truckCou = int(len(self.truckList))
        print ("",carCou ,"\t\t", busCou , "\t\t " , truckCou)
        print("---------------------")
    def checkRevenue(self):                 # COUNT ALL THE FARE THAT COME AND PUT IT IN LIST
        if int(len(self.carList)) == 0 and int(len(self.busList)) == 0 and int(len(self.truckList)) == 0 :
            print("Total Revenue : " ,"RP.0")
        else :
            carCou = int(len(self.carList))
            busCou = int(len(self.busList))
            truckCou = int(len(self.truckList))
            revenue = carCou * self.priceCar + busCou * self.priceBus + truckCou * self.priceTruck
            print("\nTotal Revenue : " ,"RP." ,revenue,"\n")
class Vehicle(TollGate):
    def CarThrough(self):
        self.carList.append(self.type)
        print("\nFare :",self.priceCar,"\n")
    def BusThrough(self):
        self.busList.append(self.type)
        print("\nFare :",self.priceBus,"\n")
    def TruckThrough(self):
        self.truckList.append(self.type)
        print("\nFare :",self.priceTruck,"\n")
x = Vehicle("Vehicle")
while True :
        print("Category of Vehicle :")
        print("1. \tCar\t\t(RP 6000)")
        print("2. \tBus\t\t(RP 8000)")
        print("3. \tTruck\t(RP 10000)")
        print("4. \tCheck Data")
        print("5. \tTotal Revenue")
        print("6. \tStop Program")
        choice=int(input("Enter choice: "))
        if choice == 1:
            x.CarThrough()
        if choice == 2:
            x.BusThrough()
        if choice == 3:
            x.TruckThrough()
        if choice == 4:
            x.checkData()
        if choice == 5:
            x.checkRevenue()
        if choice == 6:
            print("Program End byebye")
            break
