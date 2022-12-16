import re
import math

def fetch_input(filename: str="input.txt"):
    file_content = open(filename, 'r').read()
    return file_content.split('\n')

def main(filename: str="input.txt", n_top: int=2) -> int:
    _input = fetch_input(filename=filename)
    structure = build_structures(_input=_input)

    structure = run_rounds(struct=structure, rounds=20)
    for idx in range(len(structure)):
        print(f"Monkey {idx} inspected items {structure[idx]['n_items']} times.")

    n_items_list = [s["n_items"] for s in structure]
    n_items_list.sort()
    n_items_list.reverse()
    return math.prod(n_items_list[:n_top])

def run_rounds(struct: list, rounds: int):
    #print_curr_values(struct=struct, round_idx=-1)
    for r in range(rounds):
        for m in range(len(struct)):
            monkey = struct[m]
            n_items = monkey["n_items"]
            starting_items = monkey["starting_items"]

            operation = monkey["operation_new"]
            operation_op = operation["op"]
            operation_val = operation["value"]

            test = monkey["test"]
            test_div_by = test["div_by"]
            test_true_res = test["true_res"]
            test_false_res = test["false_res"]

            starting_items.reverse()
            while(len(starting_items)>0):
                obj = starting_items.pop()
                new_value = operation_new_value(value_old=obj, op=operation_op, value_2=operation_val)
                value_bored = new_value//3

                if ((value_bored%test_div_by)==0):
                    struct[test_true_res]["starting_items"].append(value_bored)
                else:
                    struct[test_false_res]["starting_items"].append(value_bored)

                n_items += 1       

            monkey["n_items"] = n_items

        #print_curr_values(struct=struct, round_idx=r)

    return struct

def print_curr_values(struct: list, round_idx: int):
    print(f"\n\nAfter round {round_idx+1}:")
    for i in range(len(struct)):
        s = struct[i]
        print(f"Monkey {i}: {s['starting_items']}")

def operation_new_value(value_old, op: str, value_2) -> int:
    v2 = value_old if (value_2=="old") else value_2

    if (op=="+"):
        return value_old + v2
    elif (op=="-"):
        return value_old - v2
    elif (op=="*"):
        return value_old * v2
    elif (op=="/"):
        return value_old // v2
    
    return 0

MONKEY_HEADER_REGEX = r"Monkey ([0-9]+):"
STARTING_ITEMS_STARTING = "  Starting items: "
STARTING_ITEMS_REGEX = r"[0-9]+"
OPERATION_NEW_REGEX = r"  Operation: new = old ([*+-/]) ([0-9]+|old)"
TEST_HEADER_REGEX = r"  Test: divisible by ([0-9]+)"
TEST_TRUE_REGEX = r"    If true: throw to monkey ([0-9]+)"
TEST_FALSE_REGEX = r"    If false: throw to monkey ([0-9]+)"
def build_structures(_input: list) -> list:
    res = []
    curr_monkey_idx = None
    struct = {}
    for row in _input:
        if ((row is None) or (len(row)==0)):
            continue

        monkey_header_regex_res = re.search(MONKEY_HEADER_REGEX, row)
        if (monkey_header_regex_res):
            if (curr_monkey_idx is not None):
                res.append(struct)
            curr_monkey_idx = int(monkey_header_regex_res.group(1))
            struct = {"n_items": 0}
            continue

        starting_items_header_res = row.startswith(STARTING_ITEMS_STARTING)
        if (starting_items_header_res):
            starting_items_regex_res = re.findall(STARTING_ITEMS_REGEX, row)
            struct["starting_items"] = [int(v) for v in starting_items_regex_res]
            continue

        operation_new_res = re.search(OPERATION_NEW_REGEX, row)
        if (operation_new_res):
            value = operation_new_res.group(2)
            if (value != "old"):
                value = int(value)

            struct["operation_new"] = {
                "op": operation_new_res.group(1),
                "value": value
            }
            continue

        test_header_regex_res = re.search(TEST_HEADER_REGEX, row)
        if (test_header_regex_res):
            struct["test"] = {
                "div_by": int(test_header_regex_res.group(1))
            }
            continue

        test_true_regex_res = re.search(TEST_TRUE_REGEX, row)
        if (test_true_regex_res):
            struct["test"]["true_res"] = int(test_true_regex_res.group(1))
            continue

        test_false_regex_res = re.search(TEST_FALSE_REGEX, row)
        if (test_false_regex_res):
            struct["test"]["false_res"] = int(test_false_regex_res.group(1))

    res.append(struct)
    return res


def main_2(filename: str="input.txt") -> str:
    _input = fetch_input(filename=filename)
    
    return None

if __name__ == '__main__':
    print(main())
    #print(main_2())
