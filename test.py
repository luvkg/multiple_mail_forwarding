class customer(object):

	def __init__(self,name,balance = 0.0):
		self.name = name
		self.balance = balance

	def withdraw(self,amount):
		if amount > self.balance:
			raise RuntimeError('amount is greater')
		self.balance -= amount
		return self.balance

	def deposite(self,amount):
		self.balance += amount
		return self.balance

jeff = customer("jeff knuth",1000.0)
print jeff.withdraw(100)