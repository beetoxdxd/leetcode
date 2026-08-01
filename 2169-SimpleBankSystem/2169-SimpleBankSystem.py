# Last updated: 1/8/2026, 5:22:04 p.m.
class Bank:

    def __init__(self, balance: List[int]):
        self.size = len(balance)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.size or account2 < 1 or account2 > self.size: return False
        if money > self.balance[account1-1]: return False
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.size: return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.size: return False
        if money > self.balance[account-1]: return False
        self.balance[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)