class Animal:
    alive = True

    def eat(self):
        print("This animal is eating .")
    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):# child of class animal
    def run(self):
        print("This rabbit is running .")
class fish(Animal):
    def swim(self):
        print("This fish is swimming .")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying .")

rabbit = Rabbit()
fish = fish()
hawk =()

#print(rabbit.alive)
#fish.eat()
rabbit.eat()

