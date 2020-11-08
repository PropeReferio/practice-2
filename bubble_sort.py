def bubble_sort(arr):
	for i in range(len(arr) - 1):
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

print(bubble_sort([4,7,1,3,90,25]))