#!/bin/bash

#students, defined as 
#students = {'name': '', 'age': '', 'email':''}

David = {'name': 'David Upegui', 'age': 22, 'email':'john_doe@email.com'}
Maria = {'name': 'Maria Allen', 'age': 24, 'email':'maria_doe@email.com'}

#Teachers, defined as 
#teachers = {'name': '', 'age': '', 'email':'', 'classes':['']}

Albert = {'name': 'Albert Ramirez', 'age': 27, 'email':'albert@email.com', 'classes':['Bash', 'Python', 'AWS']}

#Classes:
# {'Topic':'', 'teacher':'', 'students':['']}

def create_class(teacher, students, topic):
    return {'teacher': teacher, 'students': students, 'topic':topic}

course_bash = create_class(Albert, [David, Maria], 'Bash')
print(course_bash.get("teacher").get('name'))

for students in course_bash.get('students'):
    print(students.get('name'))