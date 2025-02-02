
class Employee:
    def __init__(self,name,id,department):
        self.name = name
        self.id = id
        self.department = department
def create_employee_details():
    name = input("Enter the name of the employee: ")
    id = input("Enter the id of the employee: ")
    department = input("Enter the department of the employee: ")
    emp = Employee(name,id,department)
    return emp
def main():
    create_employee_details()
main()