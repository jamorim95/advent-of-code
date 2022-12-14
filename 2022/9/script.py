import re

RIGHT_DIRECTION = "R"
LEFT_DIRECTION = "L"
UP_DIRECTION = "U"
DOWN_DIRECTION = "D"

def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n')

def main(filename: str="input.txt") -> int:
	_input = fetch_input(filename=filename)
	_input, max_steps = build_input_data(_input=_input)
	len_input = len(_input)

	start_pos = [max_steps-1, 0]
	known_positions = [start_pos]
	head_pos = [start_pos[0], start_pos[1]]
	tail_pos = [start_pos[0], start_pos[1]]

	res = 1
	prev_direction = None

	for move in _input:
		direction = move["direction"]
		steps = move["steps"]
		#print(f"direction: {direction}")
		#print(f"steps: {steps}")

		for s in range(steps):
			if direction == RIGHT_DIRECTION:
				head_pos = [head_pos[0], head_pos[1]+1]
			elif direction == LEFT_DIRECTION:
				head_pos = [head_pos[0], head_pos[1]-1]
			elif direction == UP_DIRECTION:
				head_pos = [head_pos[0]-1, head_pos[1]]
			elif direction == DOWN_DIRECTION:
				head_pos = [head_pos[0]+1, head_pos[1]]

			#print(f"\tstep {s}")
			#print(f"\tprev_direction {prev_direction}")
			#print(f"\thead_pos {head_pos}")
			#print(f"\ttail_pos {tail_pos}")	
			#print(f"\tknown_positions {known_positions}")	

			if (direction != prev_direction):
				prev_direction = direction
				continue

			flag_tail_change = False
			if direction == DOWN_DIRECTION:
				if head_pos[0]-tail_pos[0]>1:
					tail_pos[0]=head_pos[0]-1
					tail_pos[1]=head_pos[1]
					flag_tail_change = True
			elif direction == UP_DIRECTION:
				if tail_pos[0]-head_pos[0]>1:
					tail_pos[0]=head_pos[0]+1
					tail_pos[1]=head_pos[1]
					flag_tail_change = True
			elif direction == LEFT_DIRECTION:
				if tail_pos[1]-head_pos[1]>1:
					tail_pos[1]=head_pos[1]+1
					tail_pos[0]=head_pos[0]
					flag_tail_change = True
			elif direction == RIGHT_DIRECTION:
				if head_pos[1]-tail_pos[1]>1:
					tail_pos[1]=head_pos[1]-1
					tail_pos[0]=head_pos[0]
					flag_tail_change = True
			

			#print(f"TAIL_POS: {tail_pos}")
			if tail_pos not in known_positions:
				#if flag_tail_change:
				known_positions.append([tail_pos[0], tail_pos[1]])
			#elif flag_tail_change:
			#	print(f"known_positions:\n{known_positions}\n\n")

			#print(f"\ttail_pos AFTER {tail_pos}")	
		
	#print(f"\tknown_positions AFTER\n{known_positions}\n\n")	
	print_matrix(known_positions)

	return len(known_positions)

def print_matrix(known_positions: list):
	matrix = [["." for j in range(max(known_positions, key=lambda v: v[1])[1]+2)] for i in range(max(known_positions, key=lambda v: v[1])[1]+1)]
	for m in known_positions:
		matrix[m[0]][m[1]] = "#"
	
	for r in matrix:
		print(" ".join(r))
	
	print("\n")

INPUT_ROW_REGEX = r"([RLUD]{1}) ([0-9]+)"
def build_input_data(_input: list) -> list:
	res = []
	max_steps = 0

	for row in _input:
		regex_parsed_row = re.search(INPUT_ROW_REGEX, row)
		curr_steps = int(regex_parsed_row.group(2))
		res.append(
			{
				"direction": regex_parsed_row.group(1),
				"steps": curr_steps
			}
		)
		max_steps = max(max_steps, curr_steps)

	return res, max_steps


def main_2(filename: str="input.txt") -> int:
	_input = fetch_input(filename=filename)

	return None

if __name__ == '__main__':
	print(main())
	#print(main_2())

# TODO: too low  358   5831   5858