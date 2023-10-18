class BankAccount:
       
    def __init__(self, balance = 0, owner_name = 'No Data', max_debt = 0):
        self.__balance = balance
        self.__owner_name = owner_name
        self.__max_debt = max_debt

        
    def withdraw(self, amount):
        self.__amount = amount
        if self.__balance - self.__amount > self.__max_debt: 
            self.__balance = self.__balance - self.__amount
        else:
            print("The Oparation cannot be fulfilled")       
            
    def deposit(self, amount):
        self.__amount = amount
        self.__balance = self.__balance + self.__amount
        
    def get_balance(self):
        return self.__balance
    
    def set_owner_name(self, owner_name):
        self.__owner_name = owner_name
        
    def set_max_debt(self, max_debt):
        self.__max_debt = max_debt
    
    def print_balance(self):
        print(self.__balance)
        
    def set_amount(self, amount):
        self.__amount = amount
        
    def get_max_debt(self):
        return self.__max_debt

    
class Bank:
    
    def transfer(From:BankAccount, To:BankAccount, amount):
        
        if From.get_balance() - amount < From.get_max_debt():
            print("operation cannot be fulfilled")           
        else:
            From.withdraw(amount)
            To.deposit(amount)

#%%    
        
ow1 = BankAccount(1000,'XYZ',-2000)
ow2 = BankAccount(3000, 'ABC', -2000)

ow1.withdraw(100)
ow1.print_balance()
ow2.print_balance()

Bank.transfer(ow1, ow2, 100)
ow1.print_balance()
ow2.print_balance()

#%%



