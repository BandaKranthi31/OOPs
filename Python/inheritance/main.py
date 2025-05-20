class Parent:
    def speak(self):
        print("Iam the parent")

class Child(Parent):
    def greet(self):
        print("Hello from the child")

class Animal:
    def make_sound(self):
        print('eeee')

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Woof!")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")


class Truck(Vehicle):
    def __init__(self,brand,model,load_capacity):
        super().__init__(brand,model)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Load Capacity; {self.load_capacity}")



if __name__ == "__main__":
    my_truck = Truck("Volvo","K31",31)
    my_truck.display_info()
