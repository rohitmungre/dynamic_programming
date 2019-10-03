str1 = 'aab'
str2 = 'axyz'
str3 = 'aaaxybz'

def find_interleaving_dp(str1, str2, str3 , idx1, idx2, idx3, memo):
    
    mstr = str(idx1) + '~' + str(idx2) + '~' + str(idx3)
    if mstr in memo: 
        return memo[mstr]
    
    if idx3 >= len(str3): 
        memo[mstr] = True
        return True
    
    for i3 in range(idx3, len(str3)):
        
        if idx1 >= len(str1):
            if str3[i3] == str2[idx2]:
                idx2 = idx2 + 1
            else: 
                memo[mstr] = False
                return False
        elif idx2 >= len(str2):
            if str3[i3] == str1[idx1]:
                idx1 = idx1 + 1
            else: 
                memo[mstr] = False
                return False
        else:
            if str3[i3] == str1[idx1] and str3[i3] == str2[idx2]:
                res1 = find_interleaving_dp(str1, str2, str3, idx1+1, idx2, i3+1, memo)
                res2 = find_interleaving_dp(str1, str2, str3, idx1, idx2+1, i3+1, memo)
                return (res1 or res2)
            elif str3[i3] == str1[idx1]:
                idx1 = idx1 + 1
            elif str3[i3] == str2[idx2]:
                idx2 = idx2 + 1 
            else:
                memo[mstr] = False
                return False
            
    memo[mstr] = True
    return True


def find_interleaving(str1, str2, str3 , idx1, idx2, idx3):
    
    print('A', idx1, idx2, idx3)
    if idx3 >= len(str3): 
        print(idx1, idx2, idx3, idx3)
        return True
    
    for i3 in range(idx3, len(str3)):
        
        if idx1 >= len(str1):
            if str3[i3] == str2[idx2]:
                idx2 = idx2 + 1
            else: 
                print(idx1, idx2, i3)
                return False
        elif idx2 >= len(str2):
            if str3[i3] == str1[idx1]:
                idx1 = idx1 + 1
            else: 
                print(idx1, idx2, i3)
                return False
        else:
            if str3[i3] == str1[idx1] and str3[i3] == str2[idx2]:
                print('1', idx1, idx2,i3)
                res1 = find_interleaving(str1, str2, str3, idx1+1, idx2, i3+1)
                print(res1)
                res2 = find_interleaving(str1, str2, str3, idx1, idx2+1, i3+1)
                print(res2)
                return (res1 or res2)
            elif str3[i3] == str1[idx1]:
                print('2', idx1, idx2,i3)
                idx1 = idx1 + 1
            elif str3[i3] == str2[idx2]:
                print('3', idx1, idx2,i3)
                idx2 = idx2 + 1 
            else:
                print(idx1, idx2, i3)
                return False
            
    return True
    
print(find_interleaving_dp(str1, str2, str3, 0, 0, 0, {}))
