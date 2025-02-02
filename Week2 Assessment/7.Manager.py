class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def __init__(self,name,id,department):
        super().__init__(name)
        self.id = id
        self.department = department
class Manager(Employee):
    def __init__(self,name,id,department):
        super().__init__(name,id,department)
    def approve_leave(self,Employee):
        print("Leave approved for",Employee.name)

def main():
    emp=Employee("John",1,"IT")
    manager=Manager("Jane",2,"HR")
    manager.approve_leave(emp)
main()