
def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n')

def main(filename: str="input.txt") -> int:
	_input = fetch_input(filename=filename)

	_input_matrix = build_input_matrix(_input=_input)
	res = (2*len(_input_matrix)) + (2*len(_input_matrix[0])) - 4

	res += check_inner_forest(_input=_input_matrix)

	return res

def check_inner_forest(_input: list) -> int:

	res = 0

	for row_idx in range(1, len(_input)-1):
		for col_idx in range(1, len(_input[0])-1):
			curr_value = _input[row_idx][col_idx]
			_check = check_values(value=curr_value, _set=_input[row_idx], v_idx=col_idx)

			if (not _check):
				_check = check_values(value=curr_value, _set=[row[col_idx] for row in _input], v_idx=row_idx)
			
			if (_check):
				res += 1

	return res

def check_values(value: int, _set: list, v_idx: int) -> bool:
	res_lt = True
	res_gt = True

	for _idx in range(len(_set)):
		if (_idx == v_idx):
			continue
		elif ((_idx < v_idx) and (_set[_idx] >= value)):
			res_lt = False
		elif ((_idx > v_idx) and (_set[_idx] >= value)):
			res_gt = False

	return res_lt or res_gt

def build_input_matrix(_input: list) -> list:
	res = []
	res.extend([[int(v) for v in [*r]] for r in _input])

	return res

def main_2(filename: str="input.txt") -> int:
	_input = fetch_input(filename=filename)
	_input = build_input_matrix(_input=_input)

	res = []

	for row_idx in range(0, len(_input)):
		for col_idx in range(0, len(_input[0])):
			curr_value = _input[row_idx][col_idx]

			_left = _input[row_idx][:col_idx]
			_left.reverse()
			scenic_score_left = check_scenic_score(value=curr_value, _set=_left)
			
			_right = _input[row_idx][col_idx+1:]
			scenic_score_right = check_scenic_score(value=curr_value, _set=_right)
			
			_up = [row[col_idx] for row in _input[:row_idx]]
			_up.reverse()
			scenic_score_up = check_scenic_score(value=curr_value, _set=_up)
			
			_down = [row[col_idx] for row in _input[row_idx+1:]]
			scenic_score_down = check_scenic_score(value=curr_value, _set=_down)
			
			res.append(scenic_score_down*scenic_score_up*scenic_score_right*scenic_score_left)

	return max(res)

def check_scenic_score(value: int, _set: list) -> int:
	set_len = len(_set)

	for _idx in range(set_len):
		if (_set[_idx] >= value):
			return _idx + 1

	return set_len

if __name__ == '__main__':
	#print(main())
	print(main_2())
