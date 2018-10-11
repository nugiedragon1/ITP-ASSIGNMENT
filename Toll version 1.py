print("=================================================\n",
 "\tToll Payment Systems \n" ,"\tPt.Jasa Marga,Tbk\n","===============================================")        #Print the header of Toll
class TollGate():               #create a class for toll gate
    def __init__(self,type):
        self.priceCar = 6000        #define the fare for cars
        self.priceBus = 8000            #define the fare for bus
        self.priceTruck = 10000             #define the fare for truck
        self.busList =[]                   #an array for how many bus that goes through the gate
        self.carList =[]              #array for car
        self.truckList =[]         #array for truck
        self.type = type
class Vehicle(TollGate):        #a class for each vehicle
    def CarThrough(self):          #define the car that goes through the gate and append it to the list
        self.carList.append(self.type)
        print("\nFare :",self.priceCar,"\n")
    def BusThrough(self):           #define the bus that goes through the gate and append it to the bus list
        self.busList.append(self.type)
        print("\nFare :",self.priceBus,"\n")
    def TruckThrough(self):         #define the truck that goes through the gate and append it to the truck list
        self.truckList.append(self.type)
        print("\nFare :",self.priceTruck,"\n")
x= Vehicle("Vehicle")              #a is variable that posesses an object called vehicle
while True :
        print("Category of Vehicle :")
        print("1. \tCar\t\t(RP 6000)")
        print("2. \tBus\t\t(RP 8000)")
        print("3. \tTruck\t(RP 10000)")
        print("4. \tStop Program")
        choice=int(input("Enter choice: "))             #the code below is for the command
        if choice == 1:
            x.CarThrough()
        if choice == 2:
            x.BusThrough()
        if choice == 3:
            x.TruckThrough()
        if choice == 4:
            print("Program End byebye")
            break

