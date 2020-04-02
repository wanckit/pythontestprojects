def factorial(num):
    result = 1
    for x in range (1, num+1):
        result = result*x
    return result

in_variable = input ("Enter a number to calulate the factorial of")
print factorial(in_variable)
