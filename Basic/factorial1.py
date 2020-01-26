def factorial(n):
    fact = 1
    for i in range(1,n+1):
        # print(fact)
        fact = fact * i
    return fact

print(factorial(8))

