pos = [10 , 11, 9 , 12, 13, 14]

def find_trees_dp(pos, idx, memo):
    if idx in memo:
        return memo[idx]
    
    if idx == 1:
        memo[idx] =1
        return 1 
        
    if idx == 2:
        memo[idx] =2
        return 2 
        
    cleft = find_trees_dp(pos, idx-1,memo)
    cright = find_trees_dp(pos, idx-1,memo)
    csum = cleft+cright
    for i in range (1, idx-1):
        csum = csum + find_trees_dp(pos,idx-i-1,memo)*find_trees_dp(pos,i,memo)
        
    memo[idx] = csum
    return csum


def find_trees(pos, idx):
    if idx == 1:
        return 1 
        
    if idx == 2:
        return 2 
        
    cleft = find_trees(pos, idx-1)
    cright = find_trees(pos, idx-1)
    csum = cleft+cright
    for i in range (1, idx-1):
        csum = csum + find_trees(pos,idx-i-1)*find_trees(pos,i)
    
    return csum
    
print(find_trees(pos,5))
print(find_trees_dp(pos,5, {}))
