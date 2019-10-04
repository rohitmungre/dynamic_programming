import copy
arr = [2,9,1,3]

def max_profit_dp(arr, sidx, eidx, memo):
    mstr = str(sidx) + '~' + str(eidx)
    if mstr in memo:
        return memo[mstr]
    
    if sidx == eidx:
        memo[mstr] = ([arr[sidx]],None)
        return ([arr[sidx]],None)
        
    if eidx - sidx == 1: 
        memo[mstr] = ([max(arr[sidx], arr[eidx])], [min(arr[sidx],arr[eidx])])
        return ([max(arr[sidx], arr[eidx])], [min(arr[sidx],arr[eidx])])
    
    if eidx - sidx == 2: 
        memo[mstr] = ([max(arr[sidx], arr[eidx]),min(arr[sidx], arr[eidx], arr[sidx+1])], [max(arr[sidx+1], min(arr[sidx], arr[eidx]))])
        return ([max(arr[sidx], arr[eidx]),min(arr[sidx], arr[eidx], arr[sidx+1])], [max(arr[sidx+1], min(arr[sidx], arr[eidx]))])
    
    el1 = arr[sidx] 
    (rival_el1, my_el1) = max_profit_dp(arr, sidx+1, eidx, memo)
    
    el2 = arr[eidx] 
    (rival_el2, my_el2) = max_profit_dp(arr, sidx, eidx-1, memo)
    
    if sum(my_el1) + el1 > sum(my_el2) + el2:
        memo[mstr] = ( [el1]+my_el1, rival_el1)
        return ( [el1]+my_el1, rival_el1)
    else:
        memo[mstr] = ( my_el2+[el2], rival_el2)
        return ( my_el2+[el2], rival_el2)

def max_profit(arr):
    sidx = 0
    eidx = len(arr)-1
    
    if sidx == eidx:
        return ([arr[sidx]],None)
        
    if eidx - sidx == 1: 
        return ([max(arr[sidx], arr[eidx])], [min(arr[sidx],arr[eidx])])
    
    if eidx - sidx == 2: 
        return ([max(arr[sidx], arr[eidx]),min(arr[sidx], arr[eidx], arr[sidx+1])], [max(arr[sidx+1], min(arr[sidx], arr[eidx]))])
    
    carr1 = copy.copy(arr)
    el1 = carr1.pop(sidx) 
    (rival_el1, my_el1) = max_profit(carr1)
    
    carr2 = copy.copy(arr)
    el2 = carr2.pop(eidx) 
    (rival_el2, my_el2) = max_profit(carr2)
    
    if sum(my_el1) + el1 > sum(my_el2) + el2:
        return ( [el1]+my_el1, rival_el1)
    else:
        return ( my_el2+[el2], rival_el2)
        
print(max_profit([2,9,1,4,5]))
print(max_profit_dp([2,9,1,4,5],0,4,{}))
