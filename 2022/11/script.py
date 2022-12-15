import re

def fetch_input(filename: str="input.txt"):
    file_content = open(filename, 'r').read()
    return file_content.split('\n')

def main(filename: str="input.txt") -> int:
    _input = fetch_input(filename=filename)

    return None

def main_2(filename: str="input.txt") -> str:
    _input = fetch_input(filename=filename)
    
    return None

if __name__ == '__main__':
    print(main())
    #print(main_2())
