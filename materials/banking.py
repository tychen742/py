def deposit(owner, balance, amount):
    return owner, balance + amount

def withdraw(owner, balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return owner, balance - amount
