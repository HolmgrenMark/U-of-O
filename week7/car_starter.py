"""
Define a new class named "Car". 

Define the __init__() function of the Car class to take four inputs: self, model, color, and mpg. Assign the 
last three inputs to member variables of the same name by using the self keyword.
Add another attribute "condition" to your car and initialize it to "new", so when you create a new instance from Car the condition attribute of it is "new". Initilize the condition attribute inside __init__.
 

Inside the Car class, add a method named display_car() that will reference the Car's member variables to return the string, "This is a [color] [model] with [mpg] MPG. " You can use the str() function to turn your mpg into a string when creating the display string.


Inside the Car class, add a method drive_car() that sets the condition attribute to the string "used".

Inside the Car class define __str__ method such that it returns the string produced by display_car concatinated to " Car with condition: [condition of your car]".
"""

class Car(object):

	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg = mpg
		self.condition = 'new'

	def drive_car(self):
		self.condition = 'used'
	
	def display_car(self):
		return 'This i s {} {} with {} MPG.'.format(self.color, self.model, self.mpg)	

	def __str__(self):
		return '{} Car with condition: {}'.format(self.display_car(), self.condition)




		
"""
Define a child class ElectricCar that inherits all of the variables and functions from its parent class Car.   

Define __init__ for the ElectricCar, which takes the same set of arguments of constructor of its parent plus another string argument called battery_type. Inside the __init__ call the constructor of the parent class and pass the appropriate argument to it. Define an attribute for battery_type for the ElectricCar class and initialized with the corresponding argument. 
"""

class ElectricCar(Car):
	def __init__(self, modol, color, mpg, battery):

		super().__init__(modol, color, mpg)

		self.battery_type = battery

	def drive_car(self):
		self.condition = 'like new'

	#def display_car(self):
	#	return super().display_car() + 'with battery type {}'.format(self.battery_type)

	def __str__(self):
		return '{} Car with condition: {} Battery type: {}'.format(self.display_car(), self.condition, self.battery_type)


"""
Since our ElectricCar is a more specialized type of Car, 
we can give the ElectricCar its own drive_car() method that 
has different functionality than the original Car class's.
"""
"""

The drive_car() of ElecricCar changes the car's condition to the string "like new".

Inside the ElectricCar class define __str__ method such that it returns the string produced by display_car of ElectricCar concatinated to " ElectricCar with condition: [condition of your car] and battery [battery_type]".


Finally we have provided you by a main() function that creates two instances from Car and ElectricCar and calls the drive_car of each of them then prints the objects. A correct implementation of Car and ElectricCar results in the following output:

__________Befor Drive_______________
This is a black Honda with 25 MPG. Car with condition [new] 
This is a silver DeLorean with 58 MPG. ElectricCar with condition [new] and battery [molten salt] 
__________After Drive_______________
This is a black Honda with 25 MPG. Car with condition [used] 
This is a silver DeLorean with 58 MPG. ElectricCar with condition [like new] and battery [molten salt] 

"""
  
def main():
	car = Car("Honda", "black", 25 )
	e_car = ElectricCar("DeLorean", "silver", 58, "molten salt")

	print("__________Befor Drive_______________")
	print(car)
	print(e_car)

	car.drive_car()
	e_car.drive_car();


	print("__________After Drive_______________")
	print(car)
	print(e_car)

main();



