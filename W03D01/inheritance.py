# Parent Class

# Python is a duck typed and dynamically typed programming language
# we don't need to put types to the variables here.
# the variables can point to anything that we want, there is
# no restriction on what they can point in any time of execution or code flow.

class Animal:
    def __init__(self, name_of_animal):
        self.name = name_of_animal

    def speak(self):
        print("Some sound")

    def eat(self):
        print(f"{self.name} is eating")


# Cat Class is child of Animal Class
class Cat(Animal):
    def __init__(self, name_of_cat):
        super().__init__(f"Cat {name_of_cat}")


# Dog Class is child of Animal Class
class Dog(Animal):
    def __init__(self, name_of_dog):
        super().__init__(f"Dog {name_of_dog}")

    def speak(self):
        print(f"{self.name} says Woof Woof!!")


yuki_obj = Cat('Yuki')

yuki_animal = yuki_obj

mac_obj = Dog('Mac')

yuki_obj.speak()

mac_obj.speak()

mac_obj.eat()

random_animal = Animal("Hoosa")

random_animal.eat()

print(Cat.mro())
