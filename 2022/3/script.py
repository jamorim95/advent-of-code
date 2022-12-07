
_MAP = {
	"a": 1,
	"b": 2,
	"c": 3,
	"d": 4,
	"e": 5,
	"f": 6,
	"g": 7,
	"h": 8,
	"i": 9,
	"j": 10,
	"k": 11,
	"l": 12,
	"m": 13,
	"n": 14,
	"o": 15,
	"p": 16,
	"q": 17,
	"r": 18,
	"s": 19,
	"t": 20,
	"u": 21,
	"v": 22,
	"w": 23,
	"x": 24,
	"y": 25,
	"z": 26,
	"A": 27,
	"B": 28,
	"C": 29,
	"D": 30,
	"E": 31,
	"F": 32,
	"G": 33,
	"H": 34,
	"I": 35,
	"J": 36,
	"K": 37,
	"L": 38,
	"M": 39,
	"N": 40,
	"O": 41,
	"P": 42,
	"Q": 43,
	"R": 44,
	"S": 45,
	"T": 46,
	"U": 47,
	"V": 48,
	"W": 49,
	"X": 50,
	"Y": 51,
	"Z": 52
}

def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n')


def main(filename: str="input.txt"):
	res = 0
	_input = fetch_input(filename=filename)
	for rucksack in _input:
		count = {}
		_len = len(rucksack)
		comp1, comp2 = rucksack[:_len//2], rucksack[_len//2:]
		for c in comp1:
			count[c] = count.get(c, 0) + 1
		for c in comp2:
			new_count = count.get(c, 0)
			if (new_count > 0):
				res += _MAP[c]
				break
	return res

def main_2(filename: str="input.txt"):
	res = 0
	_input = fetch_input(filename=filename)

	for i in range(0,len(_input), 3):
		r_1 = _input[i]
		r_2 = _input[i+1]
		r_3 = _input[i+2]

		count = {}

		for c in r_1:
			new_value = count.get(c, {1:0,2:0})
			new_value[1] += 1
			count[c] = new_value

		for c in r_2:
			new_value = count.get(c, {1:0,2:0})
			new_value[2] += 1
			count[c] = new_value

		for c in r_3:
			new_count = count.get(c, {1:0,2:0})
			if ((new_count[1] != 0) and (new_count[2] != 0)):
				res += _MAP[c]
				break


	return res

if __name__ == '__main__':
	#print(main())
	print(main_2())
