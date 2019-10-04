st = 'abixyz'
wc = 'a*x?z'

def wc_matching_dp(st, wc, sidx, widx,memo):
    mstr = str(sidx)+'~'+str(widx)
    if mstr in memo:
        return memo[mstr]
    
    print(sidx,widx)
    if sidx >= len(st) or widx >= len(wc):
        memo[mstr] = False
        return memo[mstr]
    
    if st[sidx] == wc[widx]:
        if sidx == len(st)-1 and widx == len(wc)-1:
            memo[mstr] = True
            return memo[mstr]
        if sidx == len(st)-1 or widx == len(wc) - 1:
            memo[mstr] = False
            return memo[mstr]
        memo[mstr] = wc_matching_dp(st,wc,sidx+1,widx+1,memo)
        return memo[mstr]
        
    if wc[widx] == '?':
        memo[mstr] = wc_matching_dp(st,wc,sidx+1,widx+1,memo)
        return memo[mstr]
    if wc[widx] == '*':
        memo[mstr] = wc_matching_dp(st,wc,sidx+1,widx,memo) or wc_matching_dp(st,wc,sidx+1,widx+1,memo)
        return memo[mstr]
    memo[mstr] = False
    return memo[mstr]

def wc_matching(st, wc, sidx, widx):
    print(sidx,widx)
    if sidx >= len(st) or widx >= len(wc):
        return False
    
    if st[sidx] == wc[widx]:
        if sidx == len(st)-1 and widx == len(wc)-1:
            return True
        if sidx == len(st)-1 or widx == len(wc) - 1:
            return False
        return wc_matching(st,wc,sidx+1,widx+1)
        
    if wc[widx] == '?':
        return wc_matching(st,wc,sidx+1,widx+1)
    if wc[widx] == '*':
        return wc_matching(st,wc,sidx+1,widx) or wc_matching(st,wc,sidx+1,widx+1)
    
    return False

print(wc_matching(st,wc,0,0))
print(wc_matching_dp(st,wc,0,0,{}))
