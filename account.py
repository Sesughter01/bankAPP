class Account: ## the noun is Account
    def __init__(self, fname, lname, accnum, bvn, pin, credit, debit, amount, withdrawal, deposit): ## the properties of the account is the name, account number, bvn and the pin
        self.fname = fname
        self.lname = lname
        self.accnum = accnum
        self.bvn = bvn
        self.pin = pin
        self.credit = credit
        self.debit = debit
        self.amount = amount
        self.withdraw = withdrawal
        self.deposit = deposit

    def get_acc(self): ## the action is creating the account in the bank
        print(self.fname, self.lname + " has an account number of " + self.accnum)
        print("His BVN is " + self.bvn)
        print("His PIN is " + self.pin)

    def trans_type(self): ## the action is specifying the type of transaction performed
      print("On Feb 15 2020, you got a " + self.credit + " with an amount of " + self.amount)
      print("On Feb 16 2020, you got a " + self.debit + " with an amount of " + self.amount)
    
    def action_type(self): ## the action is specifying the action made in the account
      print("On Feb 15 2020, you " + self.deposit)
      print("On Feb 16 2020, you " + self.withdraw)

account = Account("John", "Bode", "2233445566", "123456789", "1234", "credit alert", "debit alert", "12000", "withdrawed", "deposited")
account.get_acc()
account.trans_type()
account.action_type()