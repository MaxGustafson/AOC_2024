def parse_input(file_name : str):
    print(f"file_name {file_name}")

    with open(file_name, "r") as file:
        for line in file:
            print("###")
            print(line.strip())  # .strip() removes the newline character
    

def main():
    print('Hello World')

if __name__ == '__main__':
    main()
    input_file = "input_mini.txt"
    input_file_path = "data/" + input_file
    parse_input(input_file_path)