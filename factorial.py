def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example
num = 5
print("Factorial of", num, "is", factorial(num))
