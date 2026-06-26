# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use a dummy node to simplify handling the head of the list
        k = 2
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Find the kth node
            kth = kth_node(prev_group_end.next, k)
            if not kth:
                break
            
            next_group_start = kth.next
            
            # Isolate the group to be reversed
            group_start = prev_group_end.next
            kth.next = None # Temporarily break the link
            
            # Reverse the group
            prev_group_end.next = reverseLinkedList(group_start)
            
            # After reversal, group_start is the new tail
            group_start.next = next_group_start
            
            # Prepare for the next iteration
            prev_group_end = group_start
            
        return dummy.next

def reverseLinkedList(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def kth_node(head, k):
    while head and k > 1:
        head = head.next
        k -= 1
    return head