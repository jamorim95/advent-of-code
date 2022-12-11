import re

def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n')

def main(filename: str="input.txt") -> int:
	_input = fetch_input(filename=filename)

	_input_matrix = build_input_matrix(_input=_input)
	print(f"_input_matrix: {_input_matrix}")
	res = (2*len(_input_matrix)) + (2*len(_input_matrix[0])) - 4

	res += check_inner_forest(_input=_input_matrix)

	return res

def check_inner_forest(_input: list) -> int:

	# TODO: finish

	return 0

def build_input_matrix(_input: list) -> list:
	res = []

	res.extend([[int(v) for v in [*r]] for r in _input])

	return res

if __name__ == '__main__':
	print(main())
	#print(main_2())
