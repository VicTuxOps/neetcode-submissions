class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts +=1
        BankAccount.total_balance += balance


# TODO: Create two accounts
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print("Alice's balance: ${}".format(alice.balance))
print("Bob's balance: ${}".format(bob.balance))
print("Total Accounts: {}".format(BankAccount.total_accounts))
print("Total Balance: ${}".format(BankAccount.total_balance))