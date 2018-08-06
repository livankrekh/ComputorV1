#!/Users/liabanzh/.brew/bin/python3.7

import sys
import re

def parser(polynom_str):
	matrix = [0, 0, 0]
	polynom1 = []
	polynom2 = []

	if (polynom_str.find('(') != -1 or polynom_str.find(')') != -1):
		print('Error: no bracket handling')
		exit()
	if (polynom_str.find('=') == -1)
		print('Error: no equal sign')
		exit()
	polynom_str = polynom_str.split('=')
	polynom1 = polynom_str.split(' ')
	polynom2 = polynom_str.split(' ')

	for elem in polynom1:
		if (elem.isdigit())


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Error: no polynom!")
		exit()
	parser(sys.argv[1])
