import numpy as np

def parse_input(file_name : str, debug : int = False):

    if(debug):
        print(f"file_name {file_name}")

    level_list = []
    with open(file_name, "r") as file:
        
        for line in file:
                if(debug):
                    print(f"Input line : {line}")  # .strip() removes the newline character

                val = line.strip().split()
                level_list.append([int(x) for x in val])

    return level_list

    
'''
    Return
        1 = safe
        0 = unsafe
'''
def evaluate_level(level : list, debug = False):
    if(level is None):
         raise Exception("Can't eveluate None")
    
    delta = 0
    delta_pre = 0

    for i in range(1,len(level),1):
        delta = level[i] - level[i-1]
        if debug:
            print(f"iteration {i}")
            print(f"delta = {delta}")
            print(f"delta_pre = {delta_pre}")

        if abs(delta) > 3 or\
              delta == 0 or\
                  (i != 1 and np.sign(delta) != np.sign(delta_pre)):
             return 0
             
        delta_pre = delta

    return 1

    
     
def main():
    input_file = "input.txt"
    input_file_path = "day2/data/" + input_file
    level_list = parse_input(input_file_path)

    nbr_safe : int = 0

    for i in range(len(level_list)):
        nbr_safe+=evaluate_level(level_list[i])

    print(f"Number safe levels = {nbr_safe}")
   
if __name__ == '__main__':
    main()

    