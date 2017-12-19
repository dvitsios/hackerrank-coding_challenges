def bubblesort(a):
    
    total_swaps = 0
    for i in range(len(a)):
        swaps = 0
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
                
        total_swaps += swaps
        
        if swaps == 0:
            break
            
    return str(total_swaps)


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swaps = bubblesort(a)
print('Array is sorted in '+ swaps + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[-1]))