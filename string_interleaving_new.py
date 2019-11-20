def find_interleave(s1,s2,s3, i1,i2,i3, memo):
	mstr = str(i1)+'~'+str(i2)+'~'+str(i3)
	if mstr in memo:
		return memo[mstr]
	if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
		memo[mstr] = True
		return memo[mstr]	
	if i3 == len(s3):
		memo[mstr] = False
		return memo[mstr]	
	if i1 == len(s1) and i2 == len(s2):
		memo[mstr] = False	
		return memo[mstr]	
	if s3[i3] != s1[i1:i1+1] and s3[i3] != s2[i2:i2+1]:
		memo[mstr] = False
		return memo[mstr]	
	if s3[i3] == s1[i1:i1+1] and s3[i3] == s2[i2:i2+1]:
		memo[mstr] = find_interleave(s1,s2,s3, i1+1,i2,i3+1, memo) or find_interleave(s1,s2,s3, i1,i2+1,i3+1, memo)
		return memo[mstr]	
	if s3[i3] == s1[i1:i1+1]:
		memo[mstr] = find_interleave(s1,s2,s3, i1+1,i2,i3+1, memo)		
		return memo[mstr]	
	if s3[i3] == s2[i2:i2+1]:
		memo[mstr] = find_interleave(s1,s2,s3, i1,i2+1,i3+1, memo)
		return memo[mstr]	
		
s1 = 'abc'
s2 = 'xyz'
s3 = 'abxcyz'
print(find_interleave(s1,s2,s3, 0,0,0, {}))
