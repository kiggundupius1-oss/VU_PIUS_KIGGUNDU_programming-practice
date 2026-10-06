
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def introduce(self):
        return f"Hi, I'm {self.name}, ID: {self.student_id}"


class UniversityStudent(Student):
    def __init__(self, name, age, student_id, course, year):
        # super() calls the parent's __init__
        super().__init__(name, age, student_id)
        self.course = course
        self.year = year

    
    def study(self):
        return f"{self.name} is studying {self.course} in year {self.year}"

s1 = Student("John", 18, "S001")
print(s1.introduce())

u1 = UniversityStudent("Sarah", 20, "U202", "Computer Science", 2)
print(u1.introduce()) 
print(u1.study())     