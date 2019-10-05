print('Hello World!')
import copy

boxes = [[4,4,4],[3,2,1],[5,5,5],[1,0.5,10]]
#length, width, height

def max_height(boxes, height, stck):
	print(height, stck)
	h_max = 0
	if height == 0:
		print('-------------')
		#chose all combinations one by one
		for i in range(0,len(boxes)):
			curr_box = boxes[i]
			tmp_h1 = max_height(boxes, curr_box[2], [[curr_box[0], curr_box[1], curr_box[2]]])
			print('~~~~~~',tmp_h1)
			tmp_h2 = max_height(boxes, curr_box[1], [[curr_box[0], curr_box[2], curr_box[1]]])
			print('@@@@@@',tmp_h2)
			tmp_h3 = max_height(boxes, curr_box[0], [[curr_box[2], curr_box[1], curr_box[0]]])
			print('######',tmp_h3)
			max_tmp_h = max(tmp_h1, tmp_h2, tmp_h3)
			if h_max < max_tmp_h:
				h_max = max_tmp_h
			
		return h_max
	last_box = stck[-1]
	for i in range(0,len(boxes)):
		curr_box = boxes[i]
		if last_box[0] > curr_box[0] and last_box[1]>curr_box[1]:
			stck1 = copy.copy(stck)	
			stck1.append([curr_box[0], curr_box[1], curr_box[2]])
			tmp_h = max_height(boxes, height+curr_box[2], stck1)
			if tmp_h > h_max:
				h_max = tmp_h
		elif last_box[0] > curr_box[1] and last_box[1]>curr_box[0]:
			stck1 = copy.copy(stck)	
			stck1.append([curr_box[1], curr_box[0], curr_box[2]])
			tmp_h = max_height(boxes, height+curr_box[2], stck1)
			if tmp_h > h_max:
				h_max = tmp_h
		elif last_box[0] > curr_box[0] and last_box[1]>curr_box[2]:
			stck1 = copy.copy(stck)	
			stck1.append([curr_box[0], curr_box[2], curr_box[1]])
			tmp_h = max_height(boxes, height+curr_box[1], stck1)
			if tmp_h > h_max:
				h_max = tmp_h
		elif last_box[0] > curr_box[0] and last_box[1]>curr_box[1]:
			stck1 = copy.copy(stck)	
			stck1.append([curr_box[2], curr_box[0], curr_box[1]])
			tmp_h = max_height(boxes, height+curr_box[1], stck1)
			if tmp_h > h_max:
				h_max = tmp_h
		elif last_box[0] > curr_box[2] and last_box[1]>curr_box[1]:
			stck1 = copy.copy(stck)	
			stck1.append([curr_box[2], curr_box[1], curr_box[0]])
			tmp_h = max_height(boxes, height+curr_box[0], stck1)
			if tmp_h > h_max:
				h_max = tmp_h
		elif last_box[0] > curr_box[1] and last_box[1]>curr_box[2]:
			stck1 = copy.copy(stck)	
			stck1.append([curr_box[1], curr_box[2], curr_box[0]])
			tmp_h = max_height(boxes, height+curr_box[0], stck1)	
			if tmp_h > h_max:
				h_max = tmp_h
		
	if h_max == 0:
		return height
	else:
		return h_max
	
print(max_height(boxes, 0, []))
