# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cache = set()
        curNode = head
        while curNode:
            address = hex(id(curNode))
            #address is the memory address. We can use this to differentiate, 
						# rather than by .val, as there could be duplicates at different nodes.
            if address in cache:
                return True
            cache.add(hex(id(curNode)))
            curNode = curNode.next
        return False