
def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n')


def main(filename: str="input.txt"):
	res = 0
	_input = fetch_input(filename=filename)

	for row in _input:
		set_1, set_2 = row.split(",")

		min_1, max_1 = [int(v) for v in set_1.split("-")]
		min_2, max_2 = [int(v) for v in set_2.split("-")]

		if ((min_1<=min_2) and (max_1>=max_2)):
			res += 1
		elif ((min_2<=min_1) and (max_2>=max_1)):
			res += 1
	
	return res

def main_2(filename: str="input.txt"):
	res = 0
	_input = fetch_input(filename=filename)

	for row in _input:
		set_1, set_2 = row.split(",")

		min_1, max_1 = [int(v) for v in set_1.split("-")]
		min_2, max_2 = [int(v) for v in set_2.split("-")]

		if ((max_1>=min_2) and (max_1<=max_2)) or ((max_2>=min_1) and (max_2<=max_1)):
			res += 1

	return res

if __name__ == '__main__':
	#print(main())
	print(main_2())
