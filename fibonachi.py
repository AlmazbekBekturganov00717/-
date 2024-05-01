fib1 = 1
fib2 = 2

n= int(input())

print(fib1, fib2, end="")
while fib2 < n:
   fib1, fib2 = fib2, fib1 + fib2
   print(fib2, end="")
