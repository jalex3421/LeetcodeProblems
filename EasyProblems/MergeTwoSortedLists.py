'''

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by
 splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #1)If both lists are empty
        if not list1 and not list2:
            return list1
        
        #2)If one of the given lists is empty
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        #3) If we have element in both lists
        #determine which 'head' of the lists have higher values
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        #start building our new list
        head = seek
        
        while seek and target:
            #while seek have another value and its smaller than the other list val..
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            #exchange values    
            seek.next, target = target, seek.next
            seek = seek.next
            
        return head
