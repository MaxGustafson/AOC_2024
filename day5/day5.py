def parse_input(file_name : str, debug : int = False):

    if(debug):
        print(f"file_name {file_name}")

    page_orderings = []
    update_instructions = []

    read_page_orderings = True
    read_update_instructions = False
    with open(file_name, "r") as file:
        
        for line in file:
                if(debug):
                    print(f"Input line : {line}")  # .strip() removes the newline character

                if line.strip() == "": #Reading empyt line indicates changed read mode
                    read_page_orderings = False
                    read_update_instructions = True

                elif read_page_orderings:
                    page_orderings.append(line.strip().split('|'))

                elif read_update_instructions:
                     update_instructions.append(line.strip().split(','))


    if debug:
            print("page_orderings:")
            for i in range(len(page_orderings)):
                print(page_orderings[i])
            
            print("update instructions:")
            for i in range(len(update_instructions)):
                print(update_instructions[i])

    return page_orderings, update_instructions

def build_dependency_dict(page_orderings , debug = False):
    if debug:
         print(f"Running build_dependency_dict")

    dependency_dict = {}

    '''
    Constucts dict with target element as key and a set with all elements depending on that taget as value
    '''
    for dep in page_orderings:
        target_element = dep[0]
        dependent_element = dep[1]

        if debug:
             print(f"Target Element : {target_element}")
             print(f"Dependent Element : {dependent_element}")
        if target_element not in dependency_dict:
            dependency_dict[target_element] = set()

        
        if debug:
            print(dependency_dict)
        dependency_dict[target_element].add(dependent_element)

    return dependency_dict

def evaluate_instructions(update_instructions, dependency_dict, debug = False):

    result_list = []
     
    '''
        For each instruction, compare every element in the list to subsequent elements
        to check that to dependency is broken.

        Compare list in reverse order since "element in set" is faster than "element not in set"
    '''
    for instruction in update_instructions:
        instruction_length = len(instruction)
        correct_instruction = True

        print(f"***** Evaluating: {instruction} ******")

        for i in range(instruction_length):
            for j in range (i + 1, instruction_length ,1):
                    
                current_element = instruction[instruction_length - 1 - i]
                comparing_element = instruction[instruction_length - 1 - j]

                if debug:
                    print(f"Checking if {comparing_element} can print before {current_element}")

                #No instruction for element, just skip
                if comparing_element not in dependency_dict:
                    if debug:
                        print(f"Happy skip!")
                    
                elif current_element in dependency_dict[comparing_element]:
                    if debug:
                        print(f"Happy check!")
                else:
                    correct_instruction = False
                    if debug:
                        print(f"Sad!")
        
        if correct_instruction:
            middle_index = int(instruction_length/2 -0.5) #assumes uneven list
            middle_value = int(instruction[middle_index])

            
            print(f"Adding {middle_value}")

            result_list.append(middle_value)

    return result_list


def main():

    input_file = "input_mini.txt"
    input_file_path = "day5/data/" + input_file

    page_orderings, update_instructions = parse_input(input_file_path, False)
    dependency_dict = build_dependency_dict(page_orderings, False)

    print(dependency_dict)

    result_list = evaluate_instructions(update_instructions, dependency_dict, True)

    sum = 0

    for i in result_list:
        sum+=i
    
    print(sum)



if __name__ == "__main__":
    main()