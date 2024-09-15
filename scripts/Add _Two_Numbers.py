# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode"""
        temp_node = ListNode()
        current = temp_node  
        carry = 0 
        while l1 or l2 or carry:
         if l1:
              x = l1.val
         else:
              x = 0
        
        
         if l2:
              y = l2.val
         else:
              y = 0       
         total_sum = x + y + carry
         carry = total_sum // 10                
         current.next = ListNode(total_sum % 10)                
         current = current.next
          
               

        # Move l1 and l2 pointers forward if they are not empty
         if l1:
             l1 = l1.next
         if l2:
             l2 = l2.next
    
    

    
         
        return temp_node.next  
        