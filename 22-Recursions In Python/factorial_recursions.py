#Basically recursions are functions that call function and again call function in same function

def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
print(factorial (1))