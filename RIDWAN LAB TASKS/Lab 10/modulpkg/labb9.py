class HourlyEmployee:
    def __init__(self, id, name, hours_worked, hourly_rate):
        self.id = id
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class Secretary:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def work(self, hours):
        return f"{self.name} worked for {hours} hours doing paperwork."
 

class ProductivitySystem:
    def track(self, employees, hours):
        for employee in employees:
            print(employee.work(hours))


class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print(f"Payroll for {employee.name}: ${employee.calculate_payroll():.2f}")


