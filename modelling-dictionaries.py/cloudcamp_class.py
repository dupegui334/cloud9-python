
class Student:
    
    def __init__(self, name, age, email):
        
        self.name = name
        self.age = age
        self.email = email

class Teacher:
    
    def __init__(self, name, age, email):
        
        self.name = name
        self.age = age
        self.email = email
    
    
    def set_classes(self, topics):
        self.topics = topics


#students
Pablo = Student('Pablo Peralta', 30, 'pperalta@email.com')
Ana = Student('Ana Velez', 37, 'Ana@email.com')
David = Student('David Upegui', 22, 'david@email.com')
print(type(Pablo))
print(Pablo)

#Teachers
Albert = Teacher('Albert Ramirez', 35, 'albert@email.com')
print(type(Albert))