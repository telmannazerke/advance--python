class Employee:
    def __init__(self, salary):
        self._salary = salary    

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus


def print_employees_info(employees):
    for emp in employees:
        print("Role:", emp.get_role())
        print("Salary:", emp.get_salary())
        print("-----")


e1 = Employee(150000)
e2 = Manager(300000, 50000)

staff = [e1, e2]

print_employees_info(staff)
