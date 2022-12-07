
def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n\n')


def main(filename: str="input.txt"):
	_input = fetch_input(filename=filename)
	_max = float("-inf")
	for elve in _input:
		_sum_value = sum([int(v) if ((v is not None) and (len(v)>0)) else 0 for v in elve.split('\n')])
		_max = max(_max, _sum_value)
	return _max

def main_2(filename: str="input.txt", n: int=3):
	_input = fetch_input(filename=filename)
	res=[]
	for elve in _input:
		_sum_value = sum([int(v) if ((v is not None) and (len(v)>0)) else 0 for v in elve.split('\n')])
		res.append(_sum_value)
	res.sort()
	res.reverse()
	return sum(res[:n])

if __name__ == '__main__':
	#print(main())
	print(main_2())
