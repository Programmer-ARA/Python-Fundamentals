# # ----------- QUESTION - 01 ----------
# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

class Account:
    
    def __init__(self, acc_no, balance = 0):
        self.balance = balance
        self.acc_no = acc_no

    def credit(self, credit):
        self.balance += credit
        print("Your new balance after credit is: ", self.balance)

    def debit(self, debit):
        self.balance -= debit
        print("Your new balance after debit is: ", self.balance)
    
    def get_balance(self):
        print("Your balance amount is: ", self.balance)


acc1 = Account(12345, 1000)

acc1.get_balance()
acc1.credit(500)
acc1.debit(200)
acc1.get_balance()



        

        