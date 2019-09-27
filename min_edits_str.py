str1 = 'abcdefi'
str2 = 'azcdefi'

def min_edits_dp(str1, str2, idx1, idx2, memo):
    mstr = str(idx1) + '~' + str(idx2)
    if mstr in memo:
        return memo[mstr]
    
    if idx2 == len(str2):
        return len(str1) - idx1 
     
    if idx1 == len(str1):
        return len(str2) - idx2 -1
        
    if str1[idx1] == str2[idx2]:
        return min_edits_dp(str1, str2, idx1+1, idx2+1, memo)
    
    res1 = 1+ min_edits_dp(str1, str2, idx1+1, idx2+1, memo) #edit
    res2 = 1+ min_edits_dp(str1, str2, idx1+1, idx2, memo) #delete
    res2 = 1+ min_edits_dp(str1, str2, idx1, idx2+1, memo) #add
    
    memo[mstr] = min(res1, res2)
    return min(res1, res2)


def min_edits(str1, str2, idx1, idx2):
    
    if idx2 == len(str2):
        return len(str1) - idx1 
     
    if idx1 == len(str1):
        return len(str2) - idx2 -1
        
    if str1[idx1] == str2[idx2]:
        return min_edits(str1, str2, idx1+1, idx2+1)
    
    res1 = 1+ min_edits(str1, str2, idx1+1, idx2+1) #edit
    res2 = 1+ min_edits(str1, str2, idx1+1, idx2) #delete
    res2 = 1+ min_edits(str1, str2, idx1, idx2+1) #add
    
    return min(res1, res2)
    
print(min_edits(str1, str2, 0, 0))
print(min_edits_dp(str1, str2, 0, 0, {}))
