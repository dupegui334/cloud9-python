
class User: #Master class
    
    def __init__(self, name, age, email):
        
        self.name = name
        self.age = age
        self.email = email
        
    def __str__(self):# do not print de space in memory, insted print this description
        return f"Usuario: {self.name} and mail {self.email}"
            
            
class Student(User): #Don't repeat yourself, use a hereditary class User
     pass


class Teacher(User):
    
    def set_classes(self, topics):
        self.topics = topics


class Topic: 
    
    def __init__(self, topic_name, teacher, students_list):
        self.teacher = teacher
        self.students_list = students_list
        self.topic_name = topic_name
        
    def __str__(self):# do not print de space in memory, insted print this description
        return f"The class: {self.topic_name}, teacher {self.teacher.name}, has {len(self.students_list)} students"
        
    def add_student(self, student):
        self.students_list.append(student)
        
    
#students
Pablo = Student('Pablo Peralta', 30, 'pperalta@email.com')
Ana = Student('Ana Velez', 37, 'Ana@email.com')
David = Student('David Upegui', 22, 'david@email.com')
print(type(Pablo))
print(Pablo)

#Teachers
Albert = Teacher('Albert Ramirez', 35, 'albert@email.com')
print(type(Albert))

#Topic
python_topic = Topic("Python", Albert, [David, Ana])
print(python_topic)

python_topic.add_student(Student('John Doe', 20, 'johndoe@email.com'))
print(python_topic)