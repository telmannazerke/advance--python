class Person:
    def __init__(self, name, age):
        self.name = name      
        self.age = age

    def describe(self):
        return f"Person: {self.name}, age {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   
        self.student_id = student_id

    def describe(self):
        return f"Student: {self.name}, age {self.age}, id {self.student_id}"


p = Person("Arsen", 90)
s = Student("Aida", 87, "CS2425")

objects = [p, s]

for obj in objects:
    print(obj.describe())
