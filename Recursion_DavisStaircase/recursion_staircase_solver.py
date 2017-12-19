def climb_stairs(n, d={}, ways=0):
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    if n in d:
        ways += d[n]
    else:
        ways += climb_stairs(n-1, d, ways) + climb_stairs(n-2, d, ways) + climb_stairs(n-3, d, ways)
        d[n] = ways
        
    return ways
    

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(climb_stairs(n))