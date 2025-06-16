text1=input("Enter the text to write to the file: ") 
filename = 'output.txt'

with open(filename, 'a') as file1:
    file1.write(text1 + '\n')
    print("Data successfully written to the ",filename)
    print()

text2=input("Enter additionaltext to append: ") 
with open(filename, 'a') as file1:
    file1.write(text2 + '\n')
    print("Data successfully appended.")
    print()

with open(filename, 'r') as file1:
    print("Final content of the "+ filename + ":")
    print(file1.read())     