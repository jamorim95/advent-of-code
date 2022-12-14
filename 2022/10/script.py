import re

def fetch_input(filename: str="input.txt"):
    file_content = open(filename, 'r').read()
    return file_content.split('\n')

def main(filename: str="input.txt") -> int:
    _input = fetch_input(filename=filename)
    structure = build_structure(_input=_input)

    return calc_value_for_cycles(structure=structure, cycles=[20, 60, 100, 140, 180, 220], starting_value=1)

def calc_value_for_cycles(structure: list, cycles: list, starting_value: int=1) -> int:
    res = []
    cycles_count = 0
    cumulative_count = starting_value

    for s in structure:
        value = s["value"]
        curr_cycles = s["cycles"]

        for c in range(curr_cycles):
            cycles_count += 1
            if (cycles_count in cycles):
                v = cycles_count*cumulative_count
                cycles.remove(cycles_count)

                res.append(v)
                if(len(cycles)==0):
                    return sum(res)
                
        cumulative_count += value      

    return sum(res)

NOOP_REGEX = r"noop"
ADD_REGEX = r"addx (\-?[0-9]+)"
def build_structure(_input: list) -> list:
    res = []
    for op in _input:
        noop_regex_res = re.search(NOOP_REGEX, op)
        if(noop_regex_res):
            res.append({
                "value": 0,
                "cycles": 1
            })
            continue
        
        add_regex_res = re.search(ADD_REGEX, op)
        if(add_regex_res):
            res.append({
                "value": int(add_regex_res.group(1)),
                "cycles": 2
            })
    
    return res


def main_2(filename: str="input.txt") -> str:
    _input = fetch_input(filename=filename)
    structure = build_structure(_input=_input)

    res_matrix = build_res_matrix(struct=structure)

    #return "\n".join(["".join(m) for m in res_matrix])
    return res_matrix

def build_res_matrix(struct: list) -> list:
    res = []
    _symbols = ["#", "."]
    n_symbols = len(_symbols)
    _symbols_idx = 0
    for s in struct:
        value = s["value"]
        curr_cycles = s["cycles"]

        res.append(_symbols[_symbols_idx]*curr_cycles)
        _symbols_idx = (_symbols_idx+1)%n_symbols
    
    return res



if __name__ == '__main__':
    #print(main())
    print(main_2())
