
#Classes are defined with CamelCase
#Functions and variables with Snake_case

class Dog:
    
    #Cientific name
    specie = 'Canis'
    
    #create a constructor, always the self go first, then the other parameters
    def __init__(self, name, age):
        self.name = name # In this way we save this variables in "memory"
        self.age = age
    
    def description(self):
        return f"{self.name} has {self.age} years old" #This and the line below its the same
        # return " " + str(self.name) + " has " + str(self.age) + " years old"
    
    # #Lets create a function without self
    # def bark():
    #     return "woof woof"

    #Lets create a function without self
    def bark(self, sound):
        return f"{self.name} said {sound}"
        
#Creating objects with classes
dog_1 = Dog("Nala", 5)
dog_2 = Dog("Tom", 2)

print(Dog.specie)
print(dog_1.name)
print(dog_2.name)
print(dog_1.description())
print(dog_1.bark("Woof woof"))