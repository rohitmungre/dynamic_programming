keys = [10, 11, 12]
freq = [2, 1, 2]

def btree_cost(keys, freq, sidx, eidx, memo):
    
    if sidx >= len(freq):
        return 0 
        
    if eidx <= 0: 
        return 0
    
    if sidx == eidx:
        return freq[sidx]
    
    if sidx > eidx:
        return 0

    print('---------------------')
    print(sidx , eidx)
    print('---------------------')
    
    cost_arr = []
    for ridx in range(sidx, eidx+1):
        cost_arr.append(btree_cost_withroot(keys,freq,sidx,eidx,ridx, memo))
    
    print(cost_arr)
    return min(cost_arr)
        
    
def btree_cost_withroot(keys, freq, sidx, eidx, ridx, memo):
    mstr = str(sidx)+'~'+str(eidx)+'~'+str(ridx)
    if mstr in memo:
        return memo[mstr]
    
    tbasic_cost = basic_cost(freq, sidx, eidx)
    left_cost = btree_cost(keys, freq, sidx, ridx-1, memo)
    right_cost = btree_cost(keys, freq, ridx+1, eidx, memo)
    print(sidx, eidx, ridx, tbasic_cost, left_cost, right_cost, memo)
    
    memo[mstr] = tbasic_cost + left_cost + right_cost
    return(tbasic_cost + left_cost + right_cost)
    
def basic_cost(freq, sidx, eidx):
    sm = 0
    count = sidx
    for count in range(sidx, eidx+1):
        sm = sm + freq[count]
        count = count +1 
    return sm 
    
print(basic_cost(freq, 0, 1))
print(btree_cost(keys,freq,0,2, {}))
