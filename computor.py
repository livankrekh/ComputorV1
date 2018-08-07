#!/Users/liabanzh/.brew/bin/python3.7

import sys
import re

def parser(polynom_str):
	matrix = [0, 0, 0]
	polynom1 = []
	polynom2 = []
	power = -1

	if (polynom_str.find('(') != -1 or polynom_str.find(')') != -1):
		print('Error: no bracket handling')
		exit()
	if (polynom_str.find('=') == -1):
		print('Error: no equal sign')
		exit()

	polynom_str = polynom_str.split('=')
	polynom1 = polynom_str.split(' ')
	polynom2 = polynom_str.split(' ')

	for elem in polynom1:
		if (elem.find('x') != -1 or elem.find('X') != -1):
			if (elem.find('^') != -1 and elem.find('^') + 1 < len(elem)):
				power = int(polynom1[elem.find('^') + 1:])
				if (power > 2 or power < 0):
					print("Error: Polynom power bigger than 2 or negative")
					exit()
				if (polynom1[polynom1.find(elem) - 1] == '-'):
					matrix[power] += int(elem) * -1
				else:
					matrix[power] += int(elem)



if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Error: no polynom!")
		exit()
	parser(sys.argv[1])
