

class BankAccount:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'\n Account Name: {self.name}' \
               f'\n Balance: ${self.amount}'

    def __eq__(self, other):
        return (self.name == other.name) and (other.amount == self.amount)

    def __le__(self, other):
        return self.amount <= other.amount

    def __add__(self, other):
        return self.amount + other.amount


user1 = BankAccount('Alex', 1500)
user2 = BankAccount('Alex', 1500)
print(user1 + user2)