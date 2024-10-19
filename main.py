print("Lesson 3")

class Student:
    def __init__(self,Name,Surname,Age):
        self.Name=Name
        self.Surname=Surname
        self.Age=Age
        print("Create Seccesfull")

    def print_student(self):
        print("Surname:",self.Surname,"\tName:",self.Name,"\tAge:",self.Age)


Student1 = Student("Vitalik","Oxygen",42)
Student2 = Student("Boris","Britva",24)

Student1.print_student()
Student2.print_student()

