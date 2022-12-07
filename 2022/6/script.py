
def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content

def main(filename: str="input.txt", _size: int=4) -> int:
	_input = fetch_input(filename=filename)

	for i in range(len(_input)-_size):
		curr_str = _input[i:i + _size]

		if (_size == len(set(curr_str))):
			return i+_size
	
	return None

def main_2(filename: str="input.txt") -> int:
	return main(filename=filename, _size=14)

if __name__ == '__main__':
	#print(main())
	print(main_2())
