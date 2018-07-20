import string 
import random
class Robot(object):
	name_list = []

	def __init__(self):
		self.name = "DEFAULT"
		self.reset()	
				
	def reset(self):
		while True:		
			tem_name = self.name_gen()
			if not tem_name in Robot.name_list:
				Robot.name_list.append(tem_name)
				self.name = tem_name
				break				

	def name_gen(self):
		code_part_one = random.choice(string.ascii_uppercase)
		code_part_two = random.choice(string.ascii_uppercase)
		code_part_three = random.randint(1,10)
		code_part_four = random.randint(1,10)
		code_part_five = random.randint(1,10)		
		return code_part_one + code_part_two + str(code_part_three) + str(code_part_four) + str(code_part_five)
		





	


