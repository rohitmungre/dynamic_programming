import copy 
def find_interval(s, t, idx, flag):
		
	if len(t) == 0:
		return ''
	
	if idx == len(s):
		return False
		
	if not flag and s[idx] not in t:
		return find_interval(s, t, idx+1, flag)
		
	if s[idx] not in t:
		sol =  find_interval(s, t, idx+1, flag)
		if sol == False:
			return False
		return s[idx] + sol
	
	if not flag:
		sol1 = find_interval(s, t, idx+1, False)
		temp_t = copy.copy(t)
		temp_t = temp_t.replace(s[idx], '' , 1)
		sol2 = find_interval(s, temp_t, idx+1, True)
		
		#print(idx, s, t, sol1 , sol2)
		if not sol1 and not sol2:
			return False
		elif not sol1:
			return s[idx]+ sol2
		elif not sol2: 
			return sol1   
		if len(sol1) > len(s[idx]+sol2):
			return s[idx]+sol2
		else:
			return sol1
		
	temp_t = copy.copy(t)
	temp_t = temp_t.replace(s[idx], '' , 1)
	sol = find_interval(s, temp_t, idx+1, True)
	if sol == False:
		return False
	return s[idx]+sol
	
s = 'abcdadtrteytrtet'
t = 'adda'

print(find_interval(s,t,0, False))
