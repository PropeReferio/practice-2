import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):

	def test_01(self):
		#Testing methods MUST start with 'test' or they won't run
		self.assertEqual(merge_sort([0]), [0])

	def test_02(self):
		self.assertEqual(merge_sort([5,1,3,-3,9,4]), [-3,1,3,4,5,9])

	def test_03(self):
		self.assertEqual(merge_sort(3), 'Input is not a list')

	def test_04(self):
		self.assertEqual(merge_sort([]), [])

if __name__ == '__main__':
	unittest.main()
	#Adding this block allows you to run 'python test_merge_sort.py' in the
	#terminal. Without this, you need to run 'python -m unittest test_merge_sort.py'