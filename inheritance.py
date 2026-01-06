class Employee:

    raise_amt=1.04 

    def __init__(self,first,last,pay):
        self.first=first 
        self.last=last
        self.email=first + "." + last +"@email.com" 
        self.pay=pay 
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class Developer(Employee):
    raise_amt=1.10
    def __init__(self,first,last,pay,lang):
        super().__init__(first,last,pay)
        self.lang=lang


dev_1=Developer('abhi','shek','1000000','python')
dev_2=Developer('rohit','sharma','200000','java')

print(dev_1.email)
print(dev_1.lang)

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees==None:
            self.employees=[]
        else:
            self.employees=employees 
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname())

mgr_1=Manager('Sue',"Smith","9000",[dev_1])
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
