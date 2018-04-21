import sys
import re

def getPower(str):
	if str.find('x') != -1 or str.find('X') != -1:
		if str.find('^') == -1:
			return 1
		else:
			return int(str[str.find('^') + 1])
	else:
		return 0

def parser(str_exp):
	str_exp = str_exp.replace(' ', '')
	polynom_arr = str_exp.split('=')
	res = []
	exmp = {"koff": 0, "power": 0}
	for tmp2 in polynom_arr[0].split('+'):
		if tmp2.find('-') != -1:
			split_minus = tmp2.split('-')
			exmp["koff"] = int(split_minus[0])
			exmp["power"] = getPower(split_minus[0])
			del split_minus[0]
			res.append(exmp)
			for tmp3 in split_minus:
				exmp["koff"] = int(tmp3) * -1
				exmp["power"] = getPower(tmp3)
				res.append(exmp)
		else:
			exmp["koff"] = int(tmp2)
			exmp["power"] = getPower(tmp2)
			res.append(exmp)

	print(res)

if __name__ == "__main__":
	if len(sys.argv) > 2:
		print("Error: you entered more than 1 expression!")
		exit()
	if len(sys.argv) == 1:
		print("Error: no polynom!")
		exit()
	parser(sys.argv[1])
