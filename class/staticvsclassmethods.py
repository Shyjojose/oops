class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod    #class method will change the company name for all the employees, not just the instance that calls the method.
    def change_company(cls, new_company):
        cls.company = new_company #update company name for all employees 
    @staticmethod
    def is_valid_salary(salary):
        return True if salary > 0 else False
    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}"

emp1 = Employee("Alice", 50000)
emp1.change_company("shyjo")
print(Employee.company) # Output: InnoTech
print(emp1.get_details()) # Output: Name: Alice, Salary: 50000,
print(Employee.is_valid_salary(50000)) # Output: True
print(Employee.is_valid_salary(-1000)) # Output: False
print(emp1.get_details()) # Output: Name: Alice, Salary: 50000, Company: InnoTech
print(emp1.is_valid_salary(50000)) # Output: True
print()