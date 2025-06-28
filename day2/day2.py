import numpy as np

def parse_input(file_name : str, debug : int = False):

    if(debug):
        print(f"file_name {file_name}")

    report_list = []
    with open(file_name, "r") as file:
        
        for line in file:
                if(debug):
                    print(f"Input line : {line}")  # .strip() removes the newline character

                val = line.strip().split()
                report_list.append([int(x) for x in val])

    return report_list

    
'''
    Return
        1 = safe
        0 = unsafe
'''
def evaluate_report(report : list, debug = False):
    if(report is None):
         raise Exception("Can't eveluate None")
    
    if debug:
        print(f"\n Report to evaluate {report}")
    delta = 0
    delta_pre = 0

    nbr_unsafe_levels = 0

    for i in range(1,len(report),1):
        delta = report[i] - report[i-1]
        if debug:
            print(f"iteration {i}")
            print(f"delta = {delta}")
            print(f"delta_pre = {delta_pre}")
            print(f"nbr of unsafe levels = {nbr_unsafe_levels}")

        if abs(delta) > 3 or\
              delta == 0 or\
                  (i != 1 and np.sign(delta) != np.sign(delta_pre)):
             nbr_unsafe_levels += 1
             print(f"level unsafe. nbr of unsafe levels = {nbr_unsafe_levels}")
             
        if nbr_unsafe_levels > 1:
            return 0
        delta_pre = delta

    return 1

    
     
def main(debug = False):
    input_file = "input_mini.txt"
    input_file_path = "day2/data/" + input_file
    report_list = parse_input(input_file_path)

    nbr_safe : int = 0

    for i in range(len(report_list)):
        nbr_safe+=evaluate_report(report_list[i], debug)

    print(f"\nNumber safe report = {nbr_safe}")
   
if __name__ == '__main__':
    main(True)

    