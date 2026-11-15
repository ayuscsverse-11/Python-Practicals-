"""Practical 9: Employee class."""


class Employee:
    count = 0  # class variable: number of Employee objects

    def __init__(self, emp_no, name, dept, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            raise ValueError("Basic, DA and HRA cannot be negative.")

        self.emp_no = emp_no
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra
        Employee.count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        # Decrease count when an object is destroyed
        if Employee.count > 0:
            Employee.count -= 1

    def __str__(self):
        return (f"Employee No.: {self.emp_no}\n"
                f"Name: {self.name}\n"
                f"Department: {self.dept}\n"
                f"Basic: {self.basic:.2f}\n"
                f"DA: {self.da:.2f}\n"
                f"HRA: {self.hra:.2f}\n"
                f"Total Salary: {self.salary():.2f}")


# Example
try:
    emp = Employee(
        input("Employee number: "),
        input("Name: "),
        input("Department: "),
        float(input("Basic: ")),
        float(input("DA: ")),
        float(input("HRA: "))
    )
    print("\nEmployee details")
    print(emp)
    print("Number of Employee objects:", Employee.count)
except ValueError as error:
    print("Error:", error)
