#Divide and conquer. Assumes the array is sorted.
arr = [1,5,8,23,45,67,89,100]

def binary_search(arr, element):
		#Return -1 if it's not 
		#Find the middle
		left, right = 0, len(arr)-1
		while left <= right:
				middle = (left+right) // 2
				if arr[middle] < element:
						left = middle + 1
				elif arr[middle] > element:
						right = middle - 1
				else:
						return middle
		return -1

print(binary_search(arr, 5))