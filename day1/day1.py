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
            

    

def main():
    input_file = "input_1.txt"
    input_file_path = "data/" + input_file
    list_a, list_b = parse_input(input_file_path,True)
    list_a.sort()
    list_b.sort()
    total_sum = calculate_distance(list_a, list_b,True)

    print(f"Total Distance = {total_sum}")

    

if __name__ == '__main__':
    main()
    