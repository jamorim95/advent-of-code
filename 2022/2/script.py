
_MAP = {
	"game": {
		"win": 6,
		"draw": 3,
		"loss": 0
	},
	"plays": {
		"X": {
			"name": "rock",
			"base_points": 1,
			"beats": "C",
			"beaten_by": "B"
		},
		"Y": {
			"name": "paper",
			"base_points": 2,
			"beats": "A",
			"beaten_by": "C"
		},
		"Z":  {
			"name": "scissors",
			"base_points": 3,
			"beats": "B",
			"beaten_by": "A"
		}
	}
}

_MAP_2 = {
	"plays": {
		"A": {
			"name": "rock",
			"base_points": 1,
			"beats": "Z",
			"beaten_by": "Y",
			"same_as": "X"
		},
		"B": {
			"name": "paper",
			"base_points": 2,
			"beats": "X",
			"beaten_by": "Z",
			"same_as": "Y"
		},
		"C":  {
			"name": "scissors",
			"base_points": 3,
			"beats": "Y",
			"beaten_by": "X",
			"same_as": "Z"
		}
	}
}

WIN_TOKEN = "Z"
DRAW_TOKEN = "Y"
LOSE_TOKEN = "X"

def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n')


def main(filename: str="input.txt"):
	res = 0
	_input = fetch_input(filename=filename)
	for play in _input:
		opponent, own = play.split(" ")
		_map_own = _MAP["plays"][own]
		points_game = _MAP["game"]["win"] if _map_own["beats"]==opponent else _MAP["game"]["loss"] if _map_own["beaten_by"]==opponent else _MAP["game"]["draw"]
		res += _map_own["base_points"] + points_game

	return res


def main_2(filename: str="input.txt"):
	res = 0
	_input = fetch_input(filename=filename)
	for play in _input:
		opponent, game_result = play.split(" ")
		opponent_map = _MAP_2["plays"][opponent]
		own = None
		if (game_result == WIN_TOKEN):
			own = opponent_map["beaten_by"]
		elif (game_result == LOSE_TOKEN):
			own = opponent_map["beats"]
		else:
			own = opponent_map["same_as"]
		_map_own = _MAP["plays"][own]
		points_game = _MAP["game"]["win"] if _map_own["beats"]==opponent else _MAP["game"]["loss"] if _map_own["beaten_by"]==opponent else _MAP["game"]["draw"]
		res += _map_own["base_points"] + points_game

	return res

if __name__ == '__main__':
	#print(main())
	print(main_2())
