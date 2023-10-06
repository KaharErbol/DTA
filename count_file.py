import os

def count_py_files(directory='.'):
    py_file_count = 0

    for filename in os.listdir(directory):
        if filename.endswith('.py') and os.path.isfile(os.path.join(directory, filename)):
            py_file_count += 1

    return py_file_count

if __name__ == '__main__':
    current_directory = os.getcwd()
    num_py_files = count_py_files(current_directory)
    print(f"Number of Python files in the current directory: {num_py_files}")
