def merge(a, b):
	a_idx, b_idx = 0, 0
	c = []
	while a_idx < len(a) and b_idx < len(b):
		if a[a_idx] < b[b_idx]:
			c.append(a[a_idx])
			a_idx += 1
		else:
			c.append(b[b_idx])
			b_idx += 1
	# exit...
	if a_idx < len(a):
		c.extend(a[a_idx:])
	else:
		c.extend(b[b_idx:])
	return c

print(merge([1,3,5,7], [2,4,6,8,9,10,11]))
def merge_sort(arr):
	if len(arr) == 1: return arr
	left, right = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])
	return merge(left, right)

print(merge_sort([4,1,6,9,10,2,34,21]))