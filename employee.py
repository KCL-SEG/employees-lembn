"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class WorkerContract:
    def __init__(self, commission):
        self.__commission = commission

    def get_commission(self):
        return self.__commission

    def get_description(self):
        return "worker contract"

    def get_bonus(self, contracts):
        return self.__commission * contracts

    def get_pay(self):
        return 0
    
    def get_total(self, contracts):
        return self.get_pay() + self.get_bonus(contracts)
    
class HourlyContract(WorkerContract):
    def __init__(self, rate, hours, commission = 0):
        super().__init__(commission)
        self.__rate = rate
        self.__hours = hours

    def get_pay(self):
        return self.__rate * self.__hours
    
    def __str__(self):
        return f"contract of {self.__hours} hours at {self.__rate}/hour"
    
class SalaryContract(WorkerContract):
    def __init__(self, salary, commission = 0):
        super().__init__(commission)
        self.__salary = salary

    def get_pay(self):
        return self.__salary
    
    def __str__(self):
        return f"monthly salary of {self.__salary}"

class Employee:
    def __init__(self, name, worker_contract):
        self.__name = name
        self.__worker_contract = worker_contract
        self.__contracts = 0
        self.__bonus = 0

    def add_bonus(self, bonus):
        self.__bonus += bonus 

    def add_contracts(self, contracts):
        self.__contracts += contracts
        
    def get_pay(self):
        return self.__worker_contract.get_total(self.__contracts) + self.__bonus

    def __str__(self):
        s = f"{self.__name} works on a {self.__worker_contract}"
        if self.__contracts > 0:
            s += f" and receives a commission for {self.__contracts} contract(s) at {self.__worker_contract.get_commission()}/contract"
        elif self.__bonus > 0:
            s += f" and receives a bonus commission of {self.__bonus}"
        return s + f". Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000, 200))
renee.add_contracts(4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150, 220))
jan.add_contracts(3)
print(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000))
robbie.add_bonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120))
ariel.add_bonus(600)
