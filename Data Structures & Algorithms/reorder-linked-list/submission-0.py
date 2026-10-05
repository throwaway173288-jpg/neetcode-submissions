# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        n=0
        curr=head
        indexes={}
        while curr:
            indexes[n]=curr.val
            curr=curr.next
            n+=1
        curr = head
        offset1 = 0
        offset2 = n - 1
        for i in range(n):
            if i % 2 == 0:
                curr.val = indexes[offset1]
                offset1 += 1
            else:
                curr.val = indexes[offset2]
                offset2 -= 1
            curr=curr.next

        

            
            

            
