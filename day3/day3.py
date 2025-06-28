def parse_input(file_name : str, debug : bool = False):

    if(debug):
        print(f"file_name {file_name}")

    with open(file_name, "r") as file:
        input_str = file.read()

    return input_str

'''
    Remove parts of the string which is disabled by a don't command
'''
def remove_disabled_commands(input : str, debug : bool = False):
    if debug:
        print(f"Orginal String:\n {input}")
    
    while(True):

        if 'don\'t()' not in input:
            break

        i_start = input.find('don\'t()')
        i_end = input[i_start:].find('do()') + i_start + 4 #len('do()')

        if debug:
            print(f"Removing from {i_start} to {i_end}:\n {input[i_start:i_end]}")
            print(i_start)
            print(i_end)
        
        input = input[:i_start] + input[i_end:]

    if debug:
        print(f"Returning pruned string: {input}")
    return input


def clean_input(input : str, debug : bool = True):

    input_list = input.split("mul")
    output_list = []
    if debug:
        print(input_list)

    for elem in input_list:
        if debug:
            print(f"\n evaluating elem {elem}")

        start_index = elem.find('(')
        sep_index = elem.find(',')
        stop_index = elem.find(')')

        if not (start_index != 0 or sep_index == -1 or stop_index == -1):
            factor_1 = elem[start_index+1:sep_index]
            factor_2 = elem[sep_index+1:stop_index]
            
            if factor_1.isnumeric() and factor_2.isnumeric():
                if debug:
                    print(f"Appending valid factors = {factor_1} : {factor_2}")
                output_list.append((int(factor_1),int(factor_2)))
            

        else:
            if debug:
                print("invalid_input")
            #Do nothing

    return output_list

def evaluate_cleaned_computer_commands(mul_pairs : list, debug : bool = False):
    
    total_sum = 0

    for tup in mul_pairs:
        total_sum +=tup[0] * tup[1]
        if debug:
            print(f"\nfactor_1 = {tup[0]},\n factor_2 = {tup[1]},\n product = {tup[0] * tup[1]},\n total_sum = {total_sum}\n")

    return total_sum




def main():
    input_file = "input.txt"
    input_file_path = "day3/data/" + input_file

    input_str = parse_input(input_file_path, False)
    pruned_str = remove_disabled_commands(input_str, True) #Use for part 2
    factor_pairs = clean_input(pruned_str, False)
    total_sum = evaluate_cleaned_computer_commands(factor_pairs,False)

    print(total_sum)

if __name__ == "__main__":
    main()