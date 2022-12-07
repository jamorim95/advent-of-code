import re

def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n')

CD_COMMAND_REGEX = r"\$ cd (.*)"
CD_COMMAND_BACK = ".."
LS_COMMAND_REGEX = r"\$ ls"
FILE_RES_REGEX = r"([0-9]+) (.*)"
DIR_RES_REGEX = r"dir (.*)"
def main(filename: str="input.txt", size_threshold: int=100000) -> int:
	_input = fetch_input(filename=filename)

	row = _input[0]
	cd_regex_res = re.search(CD_COMMAND_REGEX, row)
	_filesystem = check_folder(
		_input=_input,
		curr_folder=cd_regex_res.group(1),
		idx=0,
		filesystem={"folders": {}},
		parent_keys=[]
	)

	print(f"_filesystem: {_filesystem}")
	
	return None

#
#
# CICLO for PARA PERCORRER LINHA A LINHA
# SEM RECURSIVAS
#
#

def check_folder(_input: list, curr_folder: str, idx: int=0, filesystem: dict={}, parent_keys: list=[]) -> dict:
	if (curr_folder == CD_COMMAND_BACK):
		curr_folder = parent_keys.pop()
	
	row = _input[idx]

	print(f"idx: {idx}")
	print(f"curr_folder: {curr_folder}")
	print(f"filesystem:\n{filesystem}\n")
	cd_regex_res = re.search(CD_COMMAND_REGEX, row)
	if (cd_regex_res is not None):
		temp = filesystem
		
		for key in parent_keys:
			temp = temp["folders"][key]

		temp["folders"][curr_folder] = {
			"folders": {},
			"files_size": 0
		}
		
		parent_keys.append(curr_folder)
		return check_folder(
			_input=_input,
			curr_folder=cd_regex_res.group(1),
			idx=idx+1,
			filesystem=filesystem,
			parent_keys=parent_keys
		)
	
	ls_regex_res = re.search(LS_COMMAND_REGEX, row)
	if (ls_regex_res is not None):
		while((idx<len(_input)-1) and not re.search(CD_COMMAND_REGEX, _input[idx+1])):
			idx += 1
			row = _input[idx]

			dir_regex_res = re.search(DIR_RES_REGEX, row)
			if (dir_regex_res is not None):
				continue
		
			file_regex_res = re.search(FILE_RES_REGEX, row)
			if (file_regex_res is not None):
				file_size = int(file_regex_res.group(1))

				temp = filesystem
				for key in parent_keys:
					temp = temp["folders"][key]
					

				temp["files_size"] += file_size
	
	if (idx >= len(_input)-1):
		return filesystem

	return check_folder(
		_input=_input,
		curr_folder=curr_folder,
		idx=idx+1,
		filesystem=filesystem,
		parent_keys=parent_keys
	)

def main_2(filename: str="input.txt") -> int:
	return None

if __name__ == '__main__':
	print(main())
	#print(main_2())
