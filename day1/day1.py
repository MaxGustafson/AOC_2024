def parse_input(file_name : str, debug : int = False):

    if(debug):
        print(f"file_name {file_name}")

    list_a = []
    list_b = []

    with open(file_name, "r") as file:
        
        for line in file:
                val = line.strip().split()
                if(debug):
                    print(f"Input line : {line}")  # .strip() removes the newline character
                    print(f"Adding {val[0]} to list_a and {val[1]} to list_b")
        
                list_a.append(int(val[0]))
                list_b.append(int(val[1]))

    return list_a, list_b

def calculate_distance( list_a : list, list_b : list, debug = False):
    total_sum = 0

    if (list_a is None or list_b is None):
        raise Exception("One or both lists are None")
    
    n = len(list_a)
    m = len(list_b)

    if(debug):
        print("len(list_a) = {n}, len(list_b) = {m}")
     
    if(n != m):
        raise Exception("Lists of different length")
     
    if(n == 0):
        raise Exception("Trying to compare empty lists")
     
    for i in range(n):
        if(debug):
            print(f"total_sum = {total_sum}, list_a element = {list_a[i]}, list_b element = {list_a[i]}")
        total_sum += abs(list_a[i]-list_b[i])

    return total_sum 

def build_similarity_dict(input_list : list):
    similarity_dict : dict = {}

    for e in input_list:
        add_element_to_dict(e, similarity_dict)

    return similarity_dict

def add_element_to_dict(e : int, target_dict : dict):

    if(e not in target_dict):
        target_dict[e] = 0

    target_dict[e] = target_dict[e] + 1

def evaluate_similarity_score(target_list : list, similarity_dict : dict):
    score = 0

    for e in target_list:

        delta = 0
        if(e in similarity_dict):
            delta = e * similarity_dict[e]
        
        score += delta

    return score
            

    

def main():
    input_file = "input_1.txt"
    input_file_path = "data/" + input_file
    list_a, list_b = parse_input(input_file_path)
    list_a.sort()
    list_b.sort()
    total_sum = calculate_distance(list_a, list_b)

    print(f"Total Distance = {total_sum}")

def main_2():
    input_file = "input_1.txt"
    input_file_path = "data/" + input_file
    list_a, list_b = parse_input(input_file_path)
    similarity_dict = build_similarity_dict(list_b)
    score = evaluate_similarity_score(list_a, similarity_dict)
    
    print(f"Similarity Score = {score}")

    

if __name__ == '__main__':
    main()
    main_2()
    