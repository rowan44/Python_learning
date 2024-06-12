#multiple inheritance = when a child class is derived from more than one parent class
#class Organism:
#    alive = True

#class Animal(Organism):
#    def eat(self):
#        print("This animal is eating .")

#class Dog(Animal):
#    def bark(self):
#        print("This dog is barking !")
#dog = Dog()
#print(dog.alive)
#dog.bark()

#class Prey:
#    def flee(self):
#        print("This animal flees .")

#class Predator:
#    def hunt(self):
#        print("This animal is hunting")

#class Rabbit(Prey):
#    pass

#class Hawk(Predator):
#    pass

#class Fish(Prey,Predator):
#    pass
#rabbit=Rabbit()
#rabbit.flee()

class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot ")

rabbit = Rabbit()
rabbit.eat()