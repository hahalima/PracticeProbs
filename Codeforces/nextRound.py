def nextRound(n, k, ll):
    kthPlace = ll[k-1]
    counter = 0
    for element in ll:
        if (element >= kthPlace and element > 0):
            counter+=1
    return counter

n, k = map(int, raw_input().split())
ll = map(int, raw_input().split())
print nextRound(n, k, ll)
