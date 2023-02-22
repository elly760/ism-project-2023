class accounts:
    def __init__(self, name, bank, age, account_number, account_balance):
        self.name=name
        self.bank=bank
        self.age=age
        self.account_number=account_number
        self.account_balance=account_balance
    def remove(self, withdraw):
        return account_balance-withdraw
        



class withdrawn(accounts):
    
    def remove(self,withdraw):
        amount=super().remove()
        if account_balance<withdraw:
            return f"Enter the amount to withdraw"
sanga=accounts('ben', 'Stanbic', 23, 67, 500000)
sanga.remove(34444)
class deposite(accounts):
    pass
class balance(accounts):
    pass
