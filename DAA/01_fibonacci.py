"""Write a program non-recursive and recursive program to calculate Fibonacci numbers 
and analyze their time and space complexity.
"""

def fibonacci_iter(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    steps = 0
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        steps += 1
    return c, steps+1

def fibonacci_recur(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    fib1, steps1 = fibonacci_recur(n-1)
    fib2, steps2 = fibonacci_recur(n-2)
    return fib1 + fib2, steps1 + steps2 + 1

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print("Iterative:", fibonacci_iter(n)[0])
    print("Steps:", fibonacci_iter(n)[1])
    print("Recursive:", fibonacci_recur(n)[0])
    print("Steps:", fibonacci_recur(n)[1])

# way 2nd

#Non-recursion
nterms = int(input("How many terms? "))
# first two terms 
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid 
if nterms <= 0:
  print("Please enter a positive integer") 
# if there is only one term, return n1 
elif nterms == 1:
  print("Fibonacci sequence upto",nterms,":") 
  print(n1)
# generate fibonacci sequence 
else:
  print("Fibonacci sequence:") 
while count < nterms:
    print(n1)
    nth = n1 + n2
    # update values 
    n1 = n2
    n2 = nth 
    count += 1

#recursion

def recur_fibo(n):
    if n <= 1: 
       return n
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2)) 

nterms = 7

if nterms <= 0:
  print("Plese enter a positive integer") 
else:
    print("Fibonacci sequence:") 
    for i in range(nterms):
      print(recur_fibo(i))