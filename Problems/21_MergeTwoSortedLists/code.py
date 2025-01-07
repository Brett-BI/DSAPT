from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize answer ListNode to nothing, essentially
        firstNode = ListNode(-1)
        # create a tracker for the previous node and assign it to the firstNode
        # object - note that this is an assignment to the reference of the object
        previousNode = firstNode

        # while both ListNodes exist, evaluate the values of list1 and list2
        while list1 and list2:
            if list1.val <= list2.val:
                # set the next node because we know the order
                previousNode.next = list1
                list1 = list1.next 
            else:
                # set the next node because we know the order
                previousNode.next = list2
                list2 = list2.next
            
            # update the previousNode reference point to the item we just added
            previousNode = previousNode.next
        
        # list1 and/or list2 are empty so append the rest of the remaining list to 
        # the last ListNode
        previousNode.next = list1 if list1 is not None else list2

        # return the answer
        return firstNode.next

        # T: O(N + M) where N is list1 + list2 and M is firstNode + previousNode
