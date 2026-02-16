# functions
def sum(a, b):
    sum1 = a+b
    return sum1


print(sum(3, 9999))


# recursion
# call stack happens goes to end case and then backtracks to the actually case
def factorial(a):
    if (a == 1 or a == 0):
        return 1
    return factorial(a-1)*a


print(factorial(5))
