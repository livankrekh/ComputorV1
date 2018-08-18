import re

def get_power(string):
	n = str()

	if (string.find('^') != -1 and string.find('^') < len(string) - 1):
		n = string[string.find('^') + 1:]

		try:
			return int(n)
		except ValueError:
			return 1
	else:
		if (string.find('x') != -1 or string.find('X') != -1):
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
	try:
		return int(string)
	except ValueError:
		regex = re.match('\-?(x|X)\^?\d?', string)
		if (regex and len(regex.group(0)) == len(string)):
			if (string[0] == '-'):
				return -1
			else:
				return 1
		regex = re.match('\-?\d+\*?(x|X)?\^?\d*', string)
		if (regex and len(regex.group(0)) == len(string)):
			if (string.find('x') != -1 or string.find('X') != -1):
				return int(re.match('\-?\d+', string).group(0))
			return int(re.match('\-?\d+', string).group(0))
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
