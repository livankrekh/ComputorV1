#!/Users/liabanzh/.brew/bin/python3.7

import sys
import re
import tools

def toMatrix(polynom):
	matrix = [0, 0, 0]
	power = -1

	for i, elem in enumerate(polynom):
		regexObj = re.match('((\-?\d*\*?)*\-?\d*(x|X)|(\-?\d+(\*|\/))*\-?\d+)\^?\d*', elem)
		if (regexObj and len(regexObj.group(0)) == len(elem)):
			print('polynom #', i, ': \'', elem, '\'', sep='')
			power = tools.get_polynom_power(elem)
			if (power > 2 or power < 0):
				print("\033[1m\033[31mError: Polynom degree bigger than 2 or negative\033[0m")
				exit()
			matrix[power] += tools.parse_int(elem)
		else:
			print('\033[1m\033[31mWarning! Incorrect polynom member (ignored): \'', elem, '\'\033[0m', sep='')

	return matrix

def parser(polynom_str):
	matrix = []
	matrix2 = []
	polynom1 = []
	polynom2 = []

	if (polynom_str.find('(') != -1 or polynom_str.find(')') != -1):
		print('\033[1m\033[31mError: no bracket handling\033[0m')
		exit()

	polynom_str = polynom_str.split('=')
	polynom1 = list(filter(None, polynom_str[0].split(' ')))
	if (len(polynom_str) > 1):
		polynom2 = list(filter(None, polynom_str[1].split(' ')))
	else:
		print('\033[1m\033[31mWarning: no equal sign (ignored). Value by default: = 0\033[0m')

	polynom1 = tools.transform(polynom1)
	polynom2 = tools.transform(polynom2)
	print(polynom1)
	print(polynom2)
	matrix = toMatrix(polynom1)
	matrix2 = toMatrix(polynom2)

	print(matrix)
	print(matrix2)


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("\033[1m\033[31mError: no polynom!\033[0m")
		print("usage: ./computor.py \"polynom_expr\"...")
		print("every polynom member can have only one operation sign!")
		exit()

	for i in range(1, len(sys.argv)):
		parser(sys.argv[i])
