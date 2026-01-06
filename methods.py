import datetime

class Employee:
    # Class variable: default raise percentage (e.g., 1.04 for 4%)
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # TASK 1: Instance Method
    # Update self.pay by multiplying it by self.raise_amt
    def apply_raise(self):
        # TODO: Code here
        self.pay=int(self.pay*self.raise_amt)
        

    # TASK 2: Class Method (Factory)
    # Receive a string like "John-Doe-70000"
    # Parse it and return a new Employee object
    @classmethod
    def from_string(cls, emp_str):
        # TODO: Code here (Hint: use split('-'))
        first,last,pay= emp_str.split('-')
        return cls(first,last,pay)


    # TASK 3: Static Method
    # Receive a datetime.date object
    # Return False if day.weekday() == 5 (Saturday) or 6 (Sunday)
    # Otherwise return True
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

# --- TEST YOUR CODE BELOW ---

# 1. Test Instance Method
emp_1 = Employee('Corey', 'Schafer', 50000)
print(f"Original Pay: {emp_1.pay}")
emp_1.apply_raise()
print(f"New Pay: {emp_1.pay}") # Should be 52000

# 2. Test Class Method (Factory)
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(f"Created: {new_emp_1.first}, Pay: {new_emp_1.pay}") 

# 3. Test Static Method
my_date = datetime.date(2023, 7, 10) # A Monday
print(f"Is {my_date} a workday? {Employee.is_workday(my_date)}") # Should be True
