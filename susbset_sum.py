st = [2,3,7,8,10]
sm = 15

def subset_sum_dp(st, sm, idx, memo):
    if sm == 0:
        return 1
        
    if sm<0:
        return 0
    
    if idx >= len(st):
        return 0
    
    mstr = str(sm) + '~' + str(idx)
    if mstr in memo:
        return memo[mstr]
    
    res1 = subset_sum_dp(st, sm, idx+1, memo)
    res2 = subset_sum_dp(st, sm - st[idx], idx+1, memo)
    
    memo[mstr] = res1+res2
    return res1 + res2


def subset_sum(st, sm, idx):
    if sm == 0:
        return 1
        
    if sm<0:
        return 0
    
    if idx >= len(st):
        return 0
    
    res1 = subset_sum(st, sm, idx+1)
    res2 = subset_sum(st, sm - st[idx], idx+1)
    return res1 + res2
    
print(subset_sum(st, sm, 0))
print(subset_sum_dp(st, sm, 0, {}))
