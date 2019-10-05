import copy
balloons = [3,1,5,8]
balloons = [3,9,5,1]

def maximize_burst(balloons):
	if len(balloons) == 1:
		return balloons[0]
		
	h_val =0
	for i in range(0, len(balloons)):
		cballoons = copy.copy(balloons)
		if i == 0:
			tmp = 1*cballoons[0]*cballoons[1]
		elif i == len(cballoons)-1:
			tmp = 1*cballoons[i]*cballoons[i-1]
		else:
			tmp = cballoons[i-1]*cballoons[i]*cballoons[i+1]
		cballoons.pop(i)
		tmp = tmp + maximize_burst(cballoons)

		if tmp > h_val: 
			h_val = tmp
	
	return h_val	
	
print(maximize_burst(balloons))	
