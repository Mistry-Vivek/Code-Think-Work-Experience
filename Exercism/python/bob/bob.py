def hey(phrase):
	phrase = phrase.strip()
	if phrase.isupper():
		print("higher")
		if "?" in phrase:
			return "Calm down, I know what I'm doing!"
		else:	
			return "Whoa, chill out!"
	else:
		print("lower")
		if len(phrase) == 0:
			return "Fine. Be that way!"
		elif phrase[-1] == "?":
			print ("True")
			return "Sure."
		else:
			return "Whatever."
					
	pass
