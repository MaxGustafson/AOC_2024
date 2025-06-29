def parse_input(file_name : str, debug : int = False):

    if(debug):
        print(f"file_name {file_name}")

    matrix = []
    with open(file_name, "r") as file:
        
        for line in file:
                if(debug):
                    print(f"Input line : {line}")  # .strip() removes the newline character

                matrix.append(line.strip())

    if debug:
            print("Matrix:")
            for i in range(len(matrix)):
                print(matrix[i])
    return matrix

def find_xmas_in_graph(value_graph, debug : bool = False):
    ttl_nbr_xmas = 0

    '''
        Loop through entire graph and evaluate
    '''
    for i in range(len(value_graph)):
        for j in range(len(value_graph[i])):

            #straight right
            ttl_nbr_xmas += evaluate_position(value_graph, 0, 1, i, j, debug)

            #straight left
            ttl_nbr_xmas += evaluate_position(value_graph, 0, -1, i, j, debug)

            #straight up
            ttl_nbr_xmas += evaluate_position(value_graph, -1, 0, i, j, debug)

            #straight down
            ttl_nbr_xmas += evaluate_position(value_graph, 1, 0, i, j, debug)

            #diagonals
            ttl_nbr_xmas += evaluate_position(value_graph,  1, 1, i, j, debug)
            ttl_nbr_xmas += evaluate_position(value_graph,  1, -1, i, j, debug)
            ttl_nbr_xmas += evaluate_position(value_graph, -1, -1, i, j, debug)
            ttl_nbr_xmas += evaluate_position(value_graph, -1, 1, i, j, debug)

    return ttl_nbr_xmas

def evaluate_position(value_graph, x_direction, y_direction, r, c, debug):
    target_word = 'XMAS'
    max_depth = len(target_word)
    max_row = len(value_graph) 
    
    if debug and False:
        print(value_graph)
        print(f"Start at position {r},{c} -> {value_graph[r][c]}")

    for i in range(max_depth):

        if r + i*y_direction >= max_row or r + i*y_direction < 0 : #Check y in bound
            return 0
            
        max_col  = len(value_graph[r + i*y_direction]) 

        if c + i*x_direction >= max_col or c + i*x_direction < 0: #Check x in bound
            return 0

        if debug and False:
            print(f"Next position: {r + i*y_direction},{c + i*x_direction} -> {value_graph[r + i*y_direction][c + i*x_direction]}")

        if value_graph[r+ i*y_direction][c + i*x_direction] != target_word[i]: #Check letter is correct
            return 0
        
    if debug:
        print(f"Solution found:")
        for i in range(max_depth):
            print(f"{r + i*y_direction},{c + i*x_direction} -> {value_graph[r + i*y_direction][c + i*x_direction]}")
    return 1

def main():

    input_file = "input.txt"
    input_file_path = "day4/data/" + input_file

    value_graph = parse_input(input_file_path, True)
 
    ttl_nbr_xmas = find_xmas_in_graph(value_graph, True)

    print(ttl_nbr_xmas)


if __name__ == "__main__":
    main()