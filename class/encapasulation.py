class BankAccount:
	def __init__(self, owner, balance):
		self.owner = owner
		self.__balance = balance
	def deposit(self, amount):
		self.__balance = amount + self.__balance
		
	def withdraw(self, amount):
		if self.__balance > amount:
			self.__balance = self.__balance - amount
		else:
			print("insufficient balance")
	def get_balance(self):
		return self.__balance
			

account1 = BankAccount("shyjo", 1000)
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.get_balance())
print(account1.__balance)