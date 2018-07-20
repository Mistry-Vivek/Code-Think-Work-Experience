class BankAccount(object):
	def __init__(self):
		self.account_balance = 0
		self.account_state = "Neither"
								
	def get_balance(self):
		if self.account_check():
			return self.account_balance
		
	def open(self):
		if not self.account_state == "Opened":
			self.account_balance = 0   
			self.account_state = "Opened"  

	def deposit(self, amount):
		if self.account_check():
			if amount > 0:
				self.account_balance += amount
			elif amount < 0:
				raise ValueError
			return self.account_balance

	def withdraw(self, amount):
		if self.account_check():
			if amount > 0 and self.account_balance >= amount:
				self.account_balance -= amount
			else:
				raise ValueError
			return self.account_balance

	
	def close(self):
		print ("This account is now closed and can not be reaccessed")
		self.account_state = "Closed"
		

	def account_check(self):	
		if self.account_state == "Closed":
			raise ValueError
		elif self.account_state =="Opened":
			return True
		else:
			print("Account not opened yet")
			raise ValueError

