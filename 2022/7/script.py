import re

def fetch_input(filename: str="input.txt"):
	file_content = open(filename, 'r').read()
	return file_content.split('\n')

CD_COMMAND_REGEX = r"\$ cd (.*)"
CD_COMMAND_BACK = ".."
LS_COMMAND_REGEX = r"\$ ls"
FILE_RES_REGEX = r"([0-9]+) (.*)"
def main(filename: str="input.txt") -> int:
	_input = fetch_input(filename=filename)
	res = 0

	_filesystem = build_init_filesystem(_input=_input)
	for folder_key in _filesystem["folders"]:
		update_init_filesystem(_filesystem=_filesystem['folders'][folder_key])
		res += sum_prices_greater_than_threshold(_filesystem=_filesystem['folders'][folder_key])

	print(f"_filesystem:\n{_filesystem}\n")
	return res

def sum_prices_greater_than_threshold(_filesystem: dict, threshold: int=100000) -> int:
	_folders = _filesystem["folders"]
	_files_size = _filesystem["files_size"]

	if (len(_folders) == 0):
		return _files_size if _files_size <= threshold else 0
	
	res = 0
		
	for folder_key in _folders:
		res += sum_prices_greater_than_threshold(
			_filesystem=_folders[folder_key],
			threshold=threshold
		)
	
	return res + (_files_size if _files_size <= threshold else 0)


def update_init_filesystem(_filesystem: dict) -> int:
	_folders = _filesystem["folders"]
	_files_size = _filesystem["files_size"]

	if (len(_folders) == 0):
		return _files_size
	
	res =_files_size + sum([update_init_filesystem(_filesystem=_folders[f]) for f in _folders])
	_filesystem["files_size"] = res
	return res


def build_init_filesystem(_input: list) -> dict:
	filesystem={"folders": {}}
	len_input = len(_input)

	idx = 0
	parent_folders=[]
	while (True):

		###############################
		###### CD
		###############################
		
		cd_regex_res = re.search(CD_COMMAND_REGEX, _input[idx])
		flag_not_increment = False
		while(cd_regex_res):
			curr_folder=cd_regex_res.group(1)
			
			temp = filesystem["folders"]
			for key in parent_folders:
				temp = temp[key]["folders"]

			if (curr_folder == CD_COMMAND_BACK):
				curr_folder = parent_folders.pop()
			else:
				temp[curr_folder] = {"folders": {}, "files_size": 0}
				parent_folders.append(curr_folder)

			idx += 1
			if (idx >= len_input):
				return filesystem
				
			cd_regex_res = re.search(CD_COMMAND_REGEX, _input[idx])
			if (not cd_regex_res):
				flag_not_increment=True

		

		###############################
		###### ls
		###############################
		
		ls_regex_res = re.search(LS_COMMAND_REGEX, _input[idx])
		if (ls_regex_res is not None):
			while((idx<len_input-1) and not re.search(CD_COMMAND_REGEX, _input[idx+1])):
				idx += 1
				row = _input[idx]

				file_regex_res = re.search(FILE_RES_REGEX, row)
				if (file_regex_res is None):
					continue

				file_size = int(file_regex_res.group(1))

				temp = filesystem
				for folder in parent_folders:
					temp = temp["folders"][folder]
					
				temp["files_size"] += file_size
		
		if (not flag_not_increment):
			idx += 1

		if (idx >= len_input):
			return filesystem

if __name__ == '__main__':
	print(main())
	#rint(main_2())
