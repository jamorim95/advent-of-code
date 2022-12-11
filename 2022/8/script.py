
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
			print(f"[{row_idx}][{col_idx}] = {curr_value}")
			scenic_score_horizontal = check_scenic_score(value=curr_value, _set=_input[row_idx], v_idx=col_idx)
			print(f"scenic_score_horizontal: {scenic_score_horizontal}")
			scenic_score_vertical = check_scenic_score(value=curr_value, _set=[row[col_idx] for row in _input], v_idx=row_idx)
			print(f"scenic_score_vertical: {scenic_score_vertical}\n")
			res.append(scenic_score_vertical*scenic_score_horizontal)

	print(f"res: {res}")
	return max(res)

def check_scenic_score(value: int, _set: list, v_idx: int) -> int:
	res_lt = 0
	flag_lt = True

	res_gt = 0
	flag_gt = True

	# TODO: separar em right, left, up, down
	
	print(f"_set: {_set}")

	for _idx in range(len(_set)):
		if ((_idx == v_idx) and flag_lt):
			res_lt = v_idx
			print(f"[EQ] res_lt: {res_lt}")
			flag_lt = False
		elif ((_idx < v_idx) and flag_lt and (_set[_idx] >= value)):
			res_lt += v_idx - _idx
			print(f"res_lt: {res_lt}")
			flag_lt = False
		elif ((_idx > v_idx) and flag_gt and ((_set[_idx] >= value) or (_idx == (len(_set)-1)))):
			res_gt = _idx - v_idx
			print(f"res_gt: {res_gt}")
			flag_gt = False

	print(f"res_lt: {res_lt}")
	print(f"res_gt: {res_gt}")
	return res_lt * res_gt

if __name__ == '__main__':
	#print(main())
	print(main_2())
