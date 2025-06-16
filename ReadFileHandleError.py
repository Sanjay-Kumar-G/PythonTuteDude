filename = 'Sanjay.txt'
try:
    with open(filename, 'r') as file1:
        content = file1.readline()
        print("Reading file contents:")
        print("Line 1: ",content)
        content = file1.readline()
        print("Line 2: ",content)
except FileNotFoundError:
    print("Error: The file '"+filename+"' was not found.")