def longest_valid(s):
	return helper(s, 0, [[-1,0]], 0)
	
def helper(s, idx, stac, curr_max):
	print(idx, stac, curr_max)
	if idx == len(s)-1:
		if s[idx] == ')':
			sidx, l2 = stac.pop()
			if sidx == -1:
				l2 = 0
				stac.append([sidx, l2])
				return curr_max
			
			l1 = idx-sidx+1		
			pre_sidx, pre_len = stac.pop()
			pre_len = pre_len + l1		
			stac.append([pre_sidx, pre_len])
			if pre_len > curr_max:
				curr_max = pre_len
			return curr_max	
		else:
			return curr_max

	if s[idx] == '(':
		stac.append([idx,0])
		return helper(s, idx+1, stac, curr_max)		
	if s[idx] == ')':
		sidx, l2 = stac.pop()
		if sidx == -1:
			l2 = 0
			stac.append([sidx, l2])
		else:
			l1 = idx-sidx+1		
			pre_sidx, pre_len = stac.pop()
			pre_len = pre_len + l1		
			stac.append([pre_sidx, pre_len])
			if pre_len > curr_max:
				curr_max = pre_len
	curr_max = helper(s, idx+1, stac, curr_max)
	return curr_max		
	
str1 = '()()'
str2 = '((()))()'
str3 = '(((()()()))()()()'
print(longest_valid(str1))
print(longest_valid(str2))
print(longest_valid(str3))
