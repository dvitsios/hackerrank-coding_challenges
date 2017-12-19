def get_flavor_ids(money, costs):
    
    ids = {}
    
    for i in range(len(costs)):
        if costs[i] < money: 
            ids[i+1] = costs[i]
    
    exitFlag = 0
    for i in ids:
        if not exitFlag:
            for j in ids:
                if i == j:
                    continue

                if (ids[i] + ids[j]) == money:
                    print(min(i,j), max(i,j))
                    exitFlag = 1
                    break
                    
t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    get_flavor_ids(m, a)