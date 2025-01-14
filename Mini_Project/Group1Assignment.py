#Please see that there is Version 1 and 2 of the program!

#VERSION 1:

""" from abc import ABC, abstractmethod
class Vehicle (ABC): 
    def __init__ (self, regnr:str ):
        self.regnr=regnr
    @abstractmethod
    def getLicensePlate(self)->str: 
        pass 



class Car (Vehicle): 
    def __init__ (self, model:str, colour:str, electricCar:bool, regnr:str ):
        super().__init__ (regnr)
        self.model=model
        self.colour=colour
        self.electriCar=electricCar


    def getLicensePlate(self)->str:
        return self.regnr


    def isElCar(self)->bool:
        return self.electriCar 
    


class Moto (Vehicle):
    def __init__(self, offroad:bool, regnr:str):
        super().__init__ (regnr)
        self.offroad=offroad
    def getLicensePlate(self)->str:
        return self.regnr
    def isOffrd(self)->bool:
        return self.offroad


class Van (Vehicle):
    def __init__(self, numberOfSeats:int, height:float, regnr:str):
        super().__init__(regnr)
        self.numberOfSeats=numberOfSeats
        self.height=height
    def getLicensePlate(self)->str:
        return self.regnr
    def getNumOfSeats(self)->int:
        return self.numberOfSeats
    def getHeight(self)->float:
        return self.height

class Parkinglot:
    def __init__(self, name:str, location:str, capacity:int ):
        self.name=name
        self.location=location
        self.capacity=capacity
        self.currentOccupancy=0
        self.vehicles=[]
    def addVehicle(self, vehicle:Vehicle)-> bool :
        if vehicle in self.vehicles:
            return False
        if type(vehicle) is Van :
            if vehicle.getHeight () > 1.99 :
                print ("Vehicle too High")
                return False 
        else:
            self.vehicles.append(vehicle)
            self.currentOccupancy+=1
            print (f"The Vehicle with the license plate \"{vehicle.getLicensePlate()}\" has parked")
            return True  
    def removeVehicle(self, vehicle:Vehicle)-> bool : 
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            self.currentOccupancy-=1
            print (f"The Vehicle with the license plate \"{vehicle.getLicensePlate()}\" has left") 
            return True
        else:
            return False
    def getAvaliableSpots(self)->int :
        return f"{self.capacity - self.currentOccupancy} is the current capacity"
    def getOccupancyStatus(self)->str :
        return f"{self.currentOccupancy} out of {self.capacity} spots occupied"
         """






#opel=Car ("Astra", "Black", False, "DM32983")
#sonderborg=Parkinglot ("sonderborg", "Aalborg", 10)
#sonderborg.addVehicle(opel)
#print (sonderborg.getAvaliableSpots())
#print (sonderborg.getOccupancyStatus())


#isuzu=Van (9, 2.1, "CM56874")
#aa=Parkinglot ("aa", "here", 10)
#aa.addVehicle(isuzu)
#print (aa.getAvaliableSpots())
#print (aa.getOccupancyStatus())

#VERSION 2 :

from abc import ABC, abstractmethod
class ParkingLot:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.currentOccupancy = 0
        self.vehicles = []
    def addVehicle(self, vehicle):
        if isinstance(vehicle, Van) and vehicle.getHeight() > 1.99:
            print(f"Vehicle {vehicle.getLicensePlate()} is too tall to enter the university parking lot.")
            return False
        if self.currentOccupancy < self.capacity:
            self.vehicles.append(vehicle)
            self.currentOccupancy += 1
            print(f"Vehicle with the license plate '{vehicle.getLicensePlate()}' has arrived to SDU Sønderborg.")
            return True  
        print("The parking lot is full.")
        return False  
    def removeVehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            self.currentOccupancy -= 1
            print(f"Vehicle with the license plate '{vehicle.getLicensePlate()}' has left SDU Sønderborg.")
            return True  
        print(f"Vehicle with the license plate '{vehicle.getLicensePlate()}' not found.")
        return False  
    def getAvailableSpots(self):
        return self.capacity - self.currentOccupancy
    def getOccupancyStatus(self):
        return f"There are {self.currentOccupancy} spots occupied out of {self.capacity} ."
class Vehicle(ABC):
    def __init__(self, license_plate):
        self.licensePlate = license_plate
    @abstractmethod
    def getLicensePlate(self):
        pass
class Car(Vehicle):
    def __init__(self, license_plate, model, color, electrical_car):
        super().__init__(license_plate)
        self.model = model
        self.color = color
        self.electrical_car = electrical_car
    def getLicensePlate(self):
        return self.licensePlate
    def isElectricalCar(self):
        return self.electrical_car
class Motorcycle(Vehicle):
    def __init__(self, offroad, license_plate):
        super().__init__(license_plate)
        self.offroad = offroad
    def getLicensePlate(self):
        return self.licensePlate
    def isOffroad(self):
        return self.offroad
class Van(Vehicle):
    def __init__(self, numberOfSeats, height, license_plate):
        super().__init__(license_plate)
        self.numberOfSeats = numberOfSeats
        self.height = height
    def getLicensePlate(self):
        return self.licensePlate
    def getNumberOfSeats(self):
        return self.numberOfSeats
    def getHeight(self):
        return self.height
if __name__ == "__main__":
    parking_lot = ParkingLot("SDU Sønderborg", "Alsion 2", 10)
    car1 = Car("DK AGH749", "Tesla Model 3", "Red", True)
    car2 = Car("DK ABC123", "Ford Focus", "Blue", False)
    motorcycle1 = Motorcycle(True, "DK EFG456")
    van1 = Van(8, 2.5, "DK GHI789")  
    print(parking_lot.getOccupancyStatus())  
    parking_lot.addVehicle(car1)  
    print(parking_lot.getOccupancyStatus())  
    parking_lot.addVehicle(car2)  
    print(parking_lot.getOccupancyStatus())  
    parking_lot.addVehicle(motorcycle1)  
    print(parking_lot.getOccupancyStatus())  
    parking_lot.addVehicle(van1)  
    print(parking_lot.getOccupancyStatus())  
    parking_lot.removeVehicle(car1)  
    print(parking_lot.getOccupancyStatus())  
    parking_lot.removeVehicle(car2)  
    print(parking_lot.getOccupancyStatus())  


