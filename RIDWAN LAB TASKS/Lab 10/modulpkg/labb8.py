# Define the Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Define the Square class that inherits from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Define the Cube class that inherits from Square
class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        # Surface area of a cube: 6 * (side^2)
        return 6 * super().area()

    def volume(self):
        # Volume of a cube: side^3
        return self.length ** 3




class Employee:
    def __init__(self, name):
        self.name = name

    def work(self, hours):
        raise NotImplementedError("Subclasses must implement this method.")

class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Manager(SalaryEmployee):
    def work(self, hours):
        return f"{self.name} worked for {hours} hours managing the team and yelling at people."

class Secretary(SalaryEmployee):
    def work(self, hours):
        return f"{self.name} worked for {hours} hours doing paperwork and keeping things organized."

class SalesPerson(SalaryEmployee):
    def __init__(self, name, salary, commission_rate):
        super().__init__(name, salary)
        self.commission_rate = commission_rate

    def work(self, hours):
        return f"{self.name} worked for {hours} hours making sales calls."

    def calculate_commission(self, sales):
        return sales * self.commission_rate

class FactoryWorker(Employee):
    def __init__(self, name, hourly_rate):
        super().__init__(name)
        self.hourly_rate = hourly_rate

    def work(self, hours):
        return f"{self.name} worked for {hours} hours manufacturing products."

    def calculate_pay(self, hours):
        return self.hourly_rate * hours

class ProductivitySystem:
    @staticmethod
    def track(employees, hours):
        for employee in employees:
            print(employee.work(hours))



class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.staff_id}"


class AdminStaff(Staff):
    def __init__(self, name, staff_id, role):
        super().__init__(name, staff_id)
        self.role = role

    def get_details(self):
        return f"{super().get_details()}, Role: {self.role}"


class FacultyStaff(Staff):
    def __init__(self, name, staff_id, designation):
        super().__init__(name, staff_id)
        self.designation = designation

    def get_details(self):
        return f"{super().get_details()}, Designation: {self.designation}"


class Lecturer(FacultyStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Lecturer")

class AssistantProfessor(FacultyStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Assistant Professor")

class AssociateProfessor(FacultyStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Associate Professor")

class Professor(FacultyStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Professor")


class LabEngineer(AdminStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Lab Engineer")

class LabTechnician(AdminStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Lab Technician")

class LabAssistant(AdminStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Lab Assistant")

class LabAttendant(AdminStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Lab Attendant")

