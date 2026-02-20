class Account:
    def __init__(self, balance, ac_no):
        self.balance = balance
        self.ac_no = ac_no

    #debit method
    def debit(self,amount):
        self.balance -=amount
        print(f"Rs.{amount} debited from an Account. \nNew Balance: Rs.{self.balance}")
    def credit(self, amount):
        self.balance +=amount
        print(f"Rs.{amount} credited. \nNew Balance: Rs.{self.balance}")
    def get_balance(self):
        print(f"Your ac balance is Rs.{self.balance}")
ac1 = Account(100000, 123)
# ac1.debit(1000)
# ac1.credit(100000)
# ac1.get_balance()

choice = input("what do you want to check: ")
print(getattr(ac1, choice, "Not availabe"))

# choice = input("Do you want to update anything?: ")
# value = input("What do you want to change it to: ")
# setattr(ac1, choice, value)
# print(ac1.balance, "new balance")


