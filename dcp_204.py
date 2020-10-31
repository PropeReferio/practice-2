# DCP 204

# Given a complete binary tree, count the number of nodes in faster than O(n)
# time. Recall that a complete binary tree has every level filled except the 
# last, and the nodes in the last level are filled starting from the left.
class treeNode():

	def __init__(self, val):
		self.val = val
		self.leftChild = None
		self.rightChild = None

	def inorderTraversal(self, root):
		res = []
		if root:
			res = self.inorderTraversal(root.leftChild)
			res.append(root.val)
			res = res + self.inorderTraversal(root.rightChild)
		return res


# This is a complete binary tree
root = treeNode(50)
root.leftChild = treeNode(25)
root.rightChild = treeNode(75)
root.leftChild.leftChild = treeNode(12)
root.leftChild.rightChild = treeNode(37)
root.rightChild.leftChild = treeNode(63)
root.rightChild.rightChild = treeNode(87)
root.leftChild.leftChild.leftChild = treeNode(6)
root.leftChild.leftChild.rightChild = treeNode(18)
root.leftChild.rightChild.leftChild = treeNode(30)

# print(root.inorderTraversal(root))
#First, get the max depth.
def find_max_depth(root):
	if not root: return 0
	depth = 1
	curNode = root
	while curNode.leftChild:
		depth += 1
		curNode = curNode.leftChild
	return depth

def nodes_in_full_rows(depth):
	# Subtracting 1 from depth here assumes that there is at least one node in an incomplete row.
	# This is unavoidable. The next step will check what is in the final row.
	return sum([2**i for i in range(depth - 1)])

max_depth = find_max_depth(root)
complete = nodes_in_full_rows(max_depth)

print('Total nodes in complete rows: ', complete)

#next, count nodes in the bottom row, and add them to the total above
#First, check the right child of each node in the last complete row.
#Once you find None, check that nodes left child. Then you have your total.

#Now we do a DFS, looking at all the nodes of the last complete row (max_depth - 1)
empty_nodes = []
def DFS(root, depth, xCoor):
	# print(root.val)
	#It just quits after the second if block.
	if not root or depth == 0: return 0
	if depth == 3:
		#Once we find an empty node, we stop.
		# print('In the last complete row. leftChild: ', root.leftChild)
		if not root.leftChild:
			empty_nodes.append((xCoor-1) * 2)
			return (xCoor-1) * 2
		# print('In the last complete row. rightChild: ', root.rightChild)
		if not root.rightChild:
			# One more for leftChild
			empty_nodes.append((xCoor-1) * 2 + 1)
			return (xCoor-1) * 2 + 1

	else:
		# I need another parameter to track horizontal position
		# xCoor. Increment if you go right
		# xCoor needs more work. Look at root.rightChild.leftChild... in reality,
		# xCoor should be 3, but my alg puts it at 2. 
		DFS(root.leftChild, depth + 1, xCoor)
		DFS(root.rightChild, depth + 1, xCoor + 1)

last_row = DFS(root, 1, 1)
# print('Root: ', root)
# print('Nodes in last row: ', last_row)
print(empty_nodes[0])
print(empty_nodes[0] + complete)