def factorial(n):
    if n == 0:
        return 1
    # Recursive case: the factorial of n is n times the factorial of n-1
    else:
        return n * factorial(n-1)
    
result = factorial(int(input("Enter a number: ")))  
print("Factorial of",5,"is",result) 
