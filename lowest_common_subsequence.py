str1 = 'abcabcabcabcabc'
str2 = 'kkkkabcabckkabckk'

def find_lcs_dp(str1, str2, idx1, idx2, memo):
    
    if idx1 >= len(str1):
        return 0
    
    if idx2 >= len(str2):
        return 0

    mstr = str(idx1)+'~'+str(idx2)
    if mstr in memo:
        return memo[mstr]
    
    if str1[idx1] == str2[idx2]:
        return 1 + find_lcs_dp(str1, str2, idx1+1, idx2+1, memo)
        
    lcs1 = find_lcs_dp(str1, str2, idx1+1, idx2, memo)
    lcs2 = find_lcs_dp(str1, str2, idx1, idx2+1, memo)
    
    memo[mstr] = max(lcs1, lcs2)
    return max(lcs1, lcs2)


def find_lcs(str1, str2, idx1, idx2):
    
    if idx1 >= len(str1):
        return 0
    
    if idx2 >= len(str2):
        return 0

    if str1[idx1] == str2[idx2]:
        return 1 + find_lcs(str1, str2, idx1+1, idx2+1)
        
    lcs1 = find_lcs(str1, str2, idx1+1, idx2)
    lcs2 = find_lcs(str1, str2, idx1, idx2+1)
    return max(lcs1, lcs2)
    
str1 = 'abcdeab'
str2 = 'aaabbbcccdddefeeaqweb'

print(find_lcs(str1, str2, 0, 0))
print(find_lcs_dp(str1, str2, 0, 0, {}))
