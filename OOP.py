from Car import car

car_1 = car("Chevy","Corvette",2021,"blue")
car_2 = car("Ford","Mustang",2022,"red")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

#car_2.drive()
#car_2.stop()
car.wheels = 2
print(car_1.wheels)
print(car_2.wheels)