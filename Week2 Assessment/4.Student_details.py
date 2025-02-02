class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def display_student_details(self):
        return f"Name: {self.name}\nRoll Number: {self.roll_number}"
def create_student_details():
    name = input("Enter the name of the student: ")
    roll_number = input("Enter the roll number of the student: ")
    student = Student(name,roll_number)
    return student
def main():
    Students=[]
    while True:
        Students.append(create_student_details())
        choice = input("Do you want to add more students? (y/n): ")
        if choice == 'n' or choice == 'N':
            break
    for i in Students:
        print(i.display_student_details())