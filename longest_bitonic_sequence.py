seq = [2,-1,4,3,5,-1,3,2,1]

def find_bitonic(seq, idx): 
    if idx<2:
        return 0
    c_arr = []
    for i in range(1, idx-1):
        c_arr.append(find_increasing(seq, i) + find_decreasing(seq, i))
        
    return max(c_arr)
    
def find_increasing(seq, idx):
    
    if idx == 0:
        return 1
    
    tidx = idx -1 
    while seq[tidx] > seq[idx]:
        tidx = tidx -1
        if tidx < 0:
            return 1
    
    return find_increasing(seq, tidx) + 1
    
def find_decreasing(seq, idx):
    
    if idx == len(seq) - 1:
        return 1
    
    tidx = idx +1 
    while seq[tidx] > seq[idx]:
        tidx = tidx +1
        if tidx >= len(seq):
            return 1
    
    return find_decreasing(seq, tidx) + 1
    
print(find_bitonic(seq, 8))
