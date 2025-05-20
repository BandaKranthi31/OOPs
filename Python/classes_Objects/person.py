class Person:

   def __init__(self, name, age):
       self.name = name
       self.age = age


   def print_details(self):
     return f"{self.name } \n{self.age}"



if __name__ == "__main__":
    Alice = Person("Alice", 25)
    Bob = Person("Bob" , 30)

    # print(Alice.name)
    print(Alice.print_details())

