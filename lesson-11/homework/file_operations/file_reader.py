def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"An error occurred: {e}"
print(read_file(r"input.txt"))
