import sys
import re

def parser(str_exp):
	str_exp = str_exp.replace(' ', '')
	polynom_arr = str_exp.split('=')
	res = []
	tmp = {"sign": 0, "coff": 0, "power": 0}
	print(polynom_arr)

if __name__ == "__main__":
	if len(sys.argv) > 2:
		print("Error: you entered more than 1 expression!")
		exit()
	if len(sys.argv) == 1:
		print("Error: no polynom!")
		exit()
	parser(sys.argv[1])
