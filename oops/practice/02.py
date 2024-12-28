class Employee:
    def __init__(self,emp_name,emp_id,emp_salary):
        self.name = emp_name
        self.id = emp_id
        self.salary = emp_salary

    def employee_data(self):
        return f"Name: {self.name} \nID: {self.id} \nSalary: {self.salary}"
    def salary_raise(self):
        salary_raise = False
        if salary_raise:
            print("You can have a raise")
        else:
            print("You cannot have a raise")
emp1 = Employee("Heisenberg","77","5000")
print(emp1.employee_data())
emp1.salary_raise()

