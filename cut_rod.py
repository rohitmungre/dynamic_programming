rod = 7
sz = [1,2,3,4] 
vl = [2,5,7,8]

def cut_rod_dp(sz, vl, rod, idx, memo):
    if rod<= 0: 
        return 0
    
    if idx <0: 
        return 0
    
    tval = 0
    varr = []
    while rod >= 0:
        varr.append(tval+cut_rod_dp(sz, vl, rod, idx-1, memo))
        rod = rod - sz[idx]
        tval = tval + vl[idx]
    
    return max(varr)


def cut_rod(sz, vl, rod, idx):
    if rod<= 0: 
        return 0
    
    if idx <0: 
        return 0
    
    tval = 0
    varr = []
    while rod >= 0:
        varr.append(tval+cut_rod(sz, vl, rod, idx-1))
        rod = rod - sz[idx]
        tval = tval + vl[idx]
    
    return max(varr)
    
print(cut_rod_dp(sz, vl, rod, 3, {}))
