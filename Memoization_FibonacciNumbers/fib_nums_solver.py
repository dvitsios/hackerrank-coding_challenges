def fibonacci(n):
    n0 = 0
    n1 = 1
    n2 = -1
    
    for i in range(n-1):
        n2 = n0 + n1
        n0, n1 = n1, n2
    
    return n2
    
n = int(input())
print(fibonacci(n))
