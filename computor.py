#!/Users/liabanzh/.brew/bin/python3.7

import sys
import re
import tools

def toMatrix(polynom):
	matrix = [0, 0, 0]
	power = -1

	for i, elem in enumerate(polynom):
		regexObj = re.match('(\-?\d*\*?(x|X)|\-?\d+)\^?\d*', elem)
		if (regexObj and len(regexObj.group(0)) == len(elem)):
			print('polynom #', i, ': \'', elem, '\'', sep='')
			power = tools.get_power(elem)
			if ((elem.find('x') != -1 or elem.find('X') != -1) and (power > 2 or power < 0)):
				print("\033[1m\033[31mError: Polynom power bigger than 2 or negative\033[0m")
				exit()
			if (i > 0 and polynom[i - 1] == '-'):
				matrix[power] += tools.parse_int(elem) * -1
			else:
				matrix[power] += tools.parse_int(elem)
		else:
			print('\033[1m\033[31mWarning! Incorrect polynom member (ignored): \'', elem, '\'\033[0m', sep='')

	return matrix

def parser(polynom_str):
	matrix = []
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
		polynom2 = ['0']

	polynom1 = tools.transform(polynom1)
	print(polynom1)
	matrix = toMatrix(polynom1)


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("\033[1m\033[31mError: no polynom!\033[0m")
		exit()

	for i in range(1, len(sys.argv)):
		parser(sys.argv[i])
