def parse_input(file_name : str, debug : int = False):

    if(debug):
        print(f"file_name {file_name}")

    matrix = []
    with open(file_name, "r") as file:
        
        for line in file:
                if(debug):
                    print(f"Input line : {line}")  # .strip() removes the newline character

                matrix.append(line)

    if debug:
        print(f"final matrix \n {matrix}")
    return matrix

def __find_neighbors(matrix, ind_row : int, ind_col : int, max_rows : int, max_cols : int):
    """
    Finds the neighbors of a cell in a matrix.

    Args:
        matrix: The input matrix (2D list).
        ind_row: The row index of the cell.
        ind_col: The column index of the cell.

    Returns:
        A list of tuples, where each tuple represents the (row, col) of a neighbor.
    """
    neighbors = []

    # Define possible offsets for neighbors (up, down, left, right)
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (-1,1), (1,-1), (1,1)]  # Up, Down, Left, Right, Diagonals

    for row_offset, col_offset in offsets:
        new_row = ind_row + row_offset
        new_col = ind_col + col_offset

        # Check if the new coordinates are within the matrix bounds
        if 0 <= new_row < max_rows and 0 <= new_col < max_cols:
            neighbors.append((new_row, new_col))

    return neighbors

def build_neighbour_graph(matrix, debug : bool = False):

    

    n_rows = len(matrix)
    neighbour_graph = [None for i in range(n_rows)]
    for i in range(n_rows):
        n_cols = len(matrix[i])
        neighbour_graph[i] = [None for j in range(n_cols)]
        for j in range(n_cols):
            neighbour_graph[i][j] = __find_neighbors(matrix, j, i, n_rows, n_cols)

    if debug:
        print(neighbour_graph)

    return neighbour_graph

def find_xmas_in_graph(value_graph, neighbour_graph, debug : bool = False):
    ttl_nbr_xmas = 0

    '''
        Loop through entire graph and evaluate
    '''
    for i in range(len(value_graph)):
        for j in range(len(value_graph[i])):
            ttl_nbr_xmas += evaluate_position_in_graph(value_graph, neighbour_graph, i, j, 'X', debug)

    return ttl_nbr_xmas

def evaluate_position_in_graph(value_graph, neighbour_graph, r, c, target_letter, debug : bool = False):

    if debug:
        print(f"Evaluating \n Letter : {value_graph[r][c]} \n With neighbours : {neighbour_graph[r][c]} \n Target_Letter : {target_letter} ")
    match target_letter:
        case 'X':
            if value_graph[r][c] == 'X':
                for i,j in neighbour_graph[r][c]:
                    if evaluate_position_in_graph(value_graph, neighbour_graph, i, j, 'M', debug) == 1:
                        return 1
                
            return 0 

        case 'M':
            if value_graph[r][c] == 'M':
                for i,j in neighbour_graph[r][c]:
                    if evaluate_position_in_graph(value_graph, neighbour_graph, i, j, 'A', debug) == 1:
                        return 1
            
            return 0 
            
        case 'A':
            if value_graph[r][c] == 'A':
                for i,j in neighbour_graph[r][c]:
                   if evaluate_position_in_graph(value_graph, neighbour_graph, i, j, 'S', debug) == 1:
                       return 1
            
            return 0 
            
        case 'S':
            if value_graph[r][c] == 'S':
                return 1
            
            else: 
                return 0 
            
        case _ :
            return 0

             
             

def main():

    input_file = "input.txt"
    input_file_path = "day4/data/" + input_file

    value_graph = parse_input(input_file_path, True)
    neighbour_graph = build_neighbour_graph(value_graph)
    ttl_nbr_xmas = find_xmas_in_graph(value_graph, neighbour_graph, True)

    print(ttl_nbr_xmas)


if __name__ == "__main__":
    main()