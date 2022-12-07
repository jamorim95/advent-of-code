import re

def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n\n')


def main(filename: str="input.txt") -> int:
	_input = fetch_input(filename=filename)

	_board, _labels = parse_input_board(_board=_input[0])
	_board = transpose_matrix(matrix=_board)
	_board = build_labeled_board(board=_board, labels=_labels)
	_steps = parse_steps_list(steps=_input[1])

	for step in _steps:
		move = step["move"]
		_from = step["from"]
		to = step["to"]
		row_from = _board[_from]
		row_to = _board[to]

		for i in range(move):
			move_char = row_from.pop()
			row_to.append(move_char)
	
	return "".join([_board[r][-1] for r in _board])

def build_labeled_board(board: list, labels: list):
	return {
		k: v for k,v in zip(labels,board)
	}

def transpose_matrix(matrix: list) -> list:
	res = [[] for i in range(len(max(matrix, key=lambda x: len(x))))]
	for row in matrix:
		for i in range(len(row)):
			c = row[i]
			if (c is None) or (len(c)==0):
				continue

			res[i].append(c)

	return [r[-1:-len(r)-1:-1] for r in res]


BOARD_ROW_REGEX = r"(\[([A-Z]+)\]( ?))|(   )"
def parse_input_board(_board: str) -> list:
	split_board = _board.split("\n")
	
	labels = split_board[-1]
	parsed_labels = labels.strip().split("   ")
	
	rows_board = split_board[:-1]
	parsed_board_rows = []
	for row in rows_board:
		row_regex_search = [g[1] for g in re.findall(BOARD_ROW_REGEX, row)]
		parsed_board_rows.append(row_regex_search)

	return parsed_board_rows, parsed_labels

STEP_REGEX = r"move ([0-9]+) from ([0-9]+) to ([0-9]+)"
def parse_steps_list(steps: str) -> list:
	res = []

	steps_split = steps.split("\n")

	for _step in steps_split:
		_regex_search = re.search(STEP_REGEX, _step)

		move = int(_regex_search.group(1))
		_from = _regex_search.group(2)
		to = _regex_search.group(3)

		res.append({
			"move": move,
			"from": _from,
			"to": to
		})

	return res


def main_2(filename: str="input.txt") -> int:
	_input = fetch_input(filename=filename)

	_board, _labels = parse_input_board(_board=_input[0])
	_steps = parse_steps_list(steps=_input[1])
	_board = transpose_matrix(matrix=_board)
	_board = build_labeled_board(board=_board, labels=_labels)

	for step in _steps:
		move = step["move"]
		_from = step["from"]
		to = step["to"]
		row_from = _board[_from]
		row_to = _board[to]

		move_chars = [row_from.pop() for i in range(move)]
		row_to.extend(move_chars[-1:-len(move_chars)-1:-1])
	
	return "".join([_board[r][-1] for r in _board])

if __name__ == '__main__':
	#print(main())
	print(main_2())
