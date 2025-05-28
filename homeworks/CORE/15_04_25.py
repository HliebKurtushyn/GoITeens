class Employee:
    def __init__(self, name: str, salary: int, department: str):
        self.name = name
        self._salary = salary
        self.__department = department

    def increase_salary(self, increment):
        if increment > 0:
            self._salary += increment

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary > self._salary:
            self._salary = new_salary

    def get_department(self):
        return self.__department

    def __change_department(self, new_department):
        self.__department = new_department

    def set_department(self, new_department):
        self.__change_department(new_department)

Emp_1 = Employee("Gleb", 2000, "Nomer 1")

# Tests
print("Default data: Name: Gleb, Salary: 2000, Departament: Nomer 1\n")

Emp_1.increase_salary(-100)
assert Emp_1.get_salary() == 2000, "Salary should not decrease"

Emp_1.increase_salary(100)
assert Emp_1.get_salary() == 2100, "Salary should increase to 2100"

Emp_1.set_department("Nomer 2")
assert Emp_1.get_department() == "Nomer 2", "Department should change to 'Nomer 2'"

print("All test have completed successfully.")
