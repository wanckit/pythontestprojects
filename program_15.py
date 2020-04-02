def factorial(num):
    result = 1
    while num > 0:
        result = result*num
        num = num - 1
    return result

in_variable = input ("Enter a number to calulate the factorial of")
print factorial(in_variable)
