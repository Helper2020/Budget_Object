class Category:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        print('Created %s category with an initial balance of %d$' % (self.category, self.amount))

    def deposit(self, amount):
        if amount < 0:
            raise TypeError("Amount greater than zero is required")

        self.amount += amount
        print('Deposited %d$ to %s. Your new %s balance is %d$' % (amount, self.category,
                                                                   self.category, self.check_balance()))

    def check_balance(self):
        return self.amount

    def withdraw(self, amount):
        if self.amount - amount < 0:
            return 'Not enough funds.'
        else:
            self.amount -= amount
            print('Withdrew %d$ from %s. Your new %s balance is %d$' % (amount, self.category,
                                                                        self.category, self.check_balance()))

    def transfer(self, category, amount):
        print('Transferring %d$ from %s to %s' % (amount, category.category, self.category))
        self.deposit(amount)
        category.withdraw(amount)


food = Category('Food', 100)
# Deposit money
food.deposit(200)
# Withdraw money
food.withdraw(100)

print('---------------------')
entertainment = Category('Entertainment', 1000)
food.transfer(entertainment, 500)
