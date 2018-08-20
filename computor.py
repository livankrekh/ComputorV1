#!/Users/liabanzh/.brew/bin/python3.7

import sys
import re
import tools

def toMatrix(polynom):
	matrix = [0, 0, 0]
	power = -1

	for i, elem in enumerate(polynom):
		regexObj = re.match('((\-?\d*(\^\d+)?\*?)*\-?\d*(x|X)|(\-?\d+(\^\d+)?(\/?\-?\d+)?\*)*\-?\d+)\^?\d*', elem)
		if (regexObj and len(regexObj.group(0)) == len(elem)):
			power = tools.get_polynom_power(elem)
			if (power > 2 or power < 0):
				print("\033[1m\033[31mError: Polynom degree bigger than 2 or negative\033[0m")
				return None
			matrix[power] += tools.parse_int(elem)
		else:
			print('\033[1m\033[31mWarning! Incorrect polynom member (ignored): \'', elem, '\'\033[0m', sep='')

	return matrix

def parser(polynom_str, flag):
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

	if (polynom1 == None or polynom1 == None):
		return None

	matrix = toMatrix(polynom1)
	matrix2 = toMatrix(polynom2)

	if (flag):
		print("STEP 1: ", str(matrix[2]) + " * X^2 + " if matrix[2] != 0 else ""
						, str(matrix[1]) + " * X + " if matrix[1] != 0 else ""
						, str(matrix[0]) if matrix[0] != 0 else "0", " = "
						, str(matrix2[2]) + " * X^2 + " if matrix2[2] != 0 else ""
						, str(matrix2[1]) + " * X + " if matrix2[1] != 0 else ""
						, str(matrix2[0]) if matrix2[0] != 0 else "0", sep='')

	matrix[0] -= matrix2[0]
	matrix[1] -= matrix2[1]
	matrix[2] -= matrix2[2]

	print("\033[1m\033[32mPolynomial degree is:", str(tools.degree(matrix)), "\033[0m")

	print("\033[1m\033[32mReduced form: ", str(matrix[2]) + " * X^2 + " if matrix[2] != 0 else ""
						  , str(matrix[1]) + " * X + " if matrix[1] != 0 else ""
						  , str(matrix[0]) if matrix[0] != 0 else "0", " = 0\033[0m", sep='')	

	return matrix

if __name__ == "__main__":
	matrix = []
	flag = False

	if len(sys.argv) == 1:
		print("\033[1m\033[31mError: no polynom!\033[0m")
		print("usage: ./computor.py -d (for solve details) \"polynom_expr\"...")
		print("every polynom member can have only one operation sign!")
		exit()

	for i in range(1, len(sys.argv)):
		if (sys.argv[i][0] == '-'):
			if (sys.argv[i] == '-d'):
				flag = True
		else:
			print("\033[1m\033[36m___________________________\033[0m")
			matrix = parser(sys.argv[i], flag)

			if (matrix == None):
				print('Can\'t solve it!')
			elif (tools.degree(matrix) == 2):
				if (tools.descr(matrix) < 0):
					print('D < 0')
					print('\033[1m\033[32mComplex solution!\033[0m')
				elif (tools.descr(matrix) == 0):
					print('D = 0')
					print('\033[1m\033[32mThe solution is: x =', str((matrix[1] * -1) / (matrix[2] * -2)), "\033[0m")
				else:
					print('D =', tools.descr(matrix))
					print('\033[1m\033[32mThe solution is: x1 =')
			elif (tools.degree(matrix) == 1):
				print('\033[1m\033[32mThe solution is: x =', str((matrix[0] * -1) / matrix[1]), "\033[0m")
			else:
				if (matrix[0] == 0):
					print("\033[1m\033[32mThe solution is: every real number\033[0m")
				else:
					print("\033[1m\033[32mThe solution is: no one\033[0m")
