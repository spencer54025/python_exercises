def get_file_contents(filename):
    queried_file = open(filename, 'r')

    if queried_file.mode == 'r':
        return queried_file.read()

content = get_file_contents('c:/Users/night/Desktop/pythonhurrr/add_to_file/add_to_new_file.py')

print(content)

print("number of words", len(content.split()))