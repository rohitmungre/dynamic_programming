mystr = 'zagbdba'

def longest_palindromic_subsequence_dp(mystr, sidx, eidx, memo):
    
    if eidx < 0 or (sidx > eidx) or (sidx>=len(mystr)): 
        return ''
    
    if sidx == eidx: 
        return mystr[sidx]
    
    if mystr[sidx] == mystr[eidx]:
        return mystr[sidx] + longest_palindromic_subsequence_dp(mystr, sidx+1, eidx-1, memo) + mystr[eidx]
        
    s1 = longest_palindromic_subsequence_dp(mystr, sidx, eidx-1, memo)
    s2 = longest_palindromic_subsequence_dp(mystr, sidx + 1, eidx, memo)
    s3 = longest_palindromic_subsequence_dp(mystr, sidx + 1, eidx-1, memo)
    
    slist = [s1, s2, s3]
    return max(slist, key=len)


def longest_palindromic_subsequence(mystr, sidx, eidx):
    
    
    if eidx < 0 or (sidx > eidx) or (sidx>=len(mystr)): 
        return ''
    
    if sidx == eidx: 
        return mystr[sidx]
    
    if mystr[sidx] == mystr[eidx]:
        return mystr[sidx] + longest_palindromic_subsequence(mystr, sidx+1, eidx-1) + mystr[eidx]
        
    s1 = longest_palindromic_subsequence(mystr, sidx, eidx-1)
    s2 = longest_palindromic_subsequence(mystr, sidx + 1, eidx)
    s3 = longest_palindromic_subsequence(mystr, sidx + 1, eidx-1)
    
    slist = [s1, s2, s3]
    return max(slist, key=len)
    
print(longest_palindromic_subsequence(mystr, 0, 6))
print(longest_palindromic_subsequence_dp(mystr, 0, 6, {}))
