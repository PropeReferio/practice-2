# Take a singly linked list and return the reversal of it.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        curNode = head
        reverseIt = []
        while curNode:
            reverseIt.append(curNode.val)
            curNode = curNode.next
        reverseIt = reverseIt[::-1]
        newHead = ListNode(reverseIt[0])
        curNode = newHead
        for i in range(1, len(reverseIt)):
            curNode.next = ListNode()
            curNode = curNode.next
            curNode.val = reverseIt[i]
        return newHead