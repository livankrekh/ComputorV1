import re

def get_number_power(string):
	n = str()
	regex = re.match('\-?\d+', string)

	if (regex):
		if (string.find('^') != -1):
			n = string[string.find('^') + 1:]
		else:
			return 1 * int(regex.group(0))

		try:
			return power(int(regex.group(0)), int(n))
		except ValueError:
			return 1
	else:
		return 1

def get_polynom_power(string):
	n = str()

	if (string.find('x^') != -1 or string.find('X^') != -1):
		if (string.find('^') != -1):
			n = string[string.find('^') + 1:]
		else:
			return 1

		try:
			return int(n)
		except ValueError:
			return 1
	elif (string.find('x') != -1 or string.find('X') != -1):
		return 1
	else:
		return 0
			

def power(n, power):
	res = float(1)

	if (power == 0):
		return 1

	if (power > 0):
		for i in range(power):
			res *= n
	else:
		for i in range(power * -1):
			res /= n

	return res


def parse_int(string):
	expr_arr = []
	res = 0

	try:
		return int(string)
	except ValueError:
		regex = re.match('\-?(x|X)\^?\d?', string)
		if (regex and len(regex.group(0)) == len(string)):
			if (string[0] == '-'):
				return -1
			else:
				return 1
		if (string.find('*') != -1):
			res = 1
			expr_arr = string.split('*')

			for expr in expr_arr:
				regex_number = re.match('\-?\d+\^?\d*', expr)
				regex_x = re.match('\-?(x|X)\^?\d?', expr)
				regex_d = re.match('\-?\d+\/\-?\d+', expr)

				if (regex_d):
					d_arr = expr.split('/')
					res *= get_number_power(d_arr[0]) / get_number_power(d_arr[1])
				elif (regex_x):
					if (expr[0] == '-'):
						res *= -1
				elif (regex_number):
					res *= get_number_power(regex_number.group(0))

			return res
		elif (string.find('/') != -1):
			d_arr = string.split('/')
			return get_number_power(d_arr[0]) / get_number_power(d_arr[1])
		else:
			regex_new = re.match('\-?\d+\^?\d*', string)

			if (regex_new):
				return get_number_power(regex_new.group(0))
			else:
				return 0

def isSign(string):
	regex = re.match('(\-|\+|\*|\/|\^)+', string)

	if (regex and len(regex.group(0)) == len(string)):
		return True
	return False

def transform(arr):
	new_arr = []

	for i, elem in enumerate(arr):
		if (elem == '-' and i < len(arr) - 1):
			if (len(arr[i + 1]) > 0 and arr[i + 1][0] == '-'):
				arr[i + 1] = arr[i + 1][1:]
			else:
				arr[i + 1] = "-" + arr[i + 1]
		elif ((elem == '*' or elem == '/' or elem == '^') and i > 0 and i < len(arr) - 1):
			arr[i + 1] = arr[i - 1] + arr[i] + arr[i + 1]
			arr[i - 1] = ''

	for i, elem in enumerate(arr):
		if (elem != '' and not isSign(elem)):
			new_arr.append(elem);

	return (new_arr)
