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

	#matrix = [[0 for j in range(max_steps)] for i in range(max_steps)]

	len_input = len(_input)
	start_pos = [(len_input*max_steps)+1, (len_input*max_steps)+1]
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
				#print("\n\n")
				prev_direction = direction
				continue

			if direction == DOWN_DIRECTION:
				if head_pos[0]-tail_pos[0]>1:
					tail_pos[0]=head_pos[0]-1
					tail_pos[1]=head_pos[1]
			elif direction == UP_DIRECTION:
				if tail_pos[0]-head_pos[0]>1:
					tail_pos[0]=head_pos[0]+1
					tail_pos[1]=head_pos[1]
			elif direction == LEFT_DIRECTION:
				if tail_pos[1]-head_pos[1]>1:
					tail_pos[1]=head_pos[1]+1
					tail_pos[0]=head_pos[0]
			elif direction == RIGHT_DIRECTION:
				if head_pos[1]-tail_pos[1]>1:
					tail_pos[1]=head_pos[1]-1
					tail_pos[0]=head_pos[0]
			
			if tail_pos not in known_positions:
				known_positions.append([tail_pos[0], tail_pos[1]])
			#print(f"\ttail_pos AFTER {tail_pos}")	
			#print(f"\tknown_positions AFTER {known_positions}\n\n")	

	return len(known_positions)

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

# TODO: too low  358   5858   