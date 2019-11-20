def longest_with_k(S, k, start, stop, memo):
	mstr = str(start)+'~'+str(stop)
	if mstr in memo:
		return memo[mstr]
	chars = find_unique_chars(S[start:stop+1])
	if stop == len(S) - 1:
		if chars == k:
			return stop - start + 1
		else:
			return 0		
	sol2 = longest_with_k(S,k, start+1, start+k+1, memo)
	if chars>k:
		memo[mstr] = sol2
		return sol2
	else:
		sol1 = longest_with_k(S,k,start, stop+1, memo)
		if chars == k: 
			sol3 = stop - start + 1
		else:
			sol3 = 0
		memo[mstr] = max(sol1, sol2, sol3)	
		return memo[mstr]
	
	
def find_unique_chars(S):
	ulist = []
	for i in range(len(S)):
		if S[i] not in ulist:
			ulist.append(S[i])	
	return len(ulist)	
	
S = 'abcabcaabbcccccd'
k = 5
print(longest_with_k(S,k,0,k-1, {}))
