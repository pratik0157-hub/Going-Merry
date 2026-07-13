#!/usr/bin/env python3

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of 
their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""

# My solution:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        num1 = 0
        factor1 = 1
        while l1:
            num1 += l1.val * factor1
            factor1 *= 10
            l1 = l1.next  

        num2 = 0
        factor2 = 1
        while l2:
            num2 += l2.val * factor2
            factor2 *= 10
            l2 = l2.next  
            
        
        total_sum = num1 + num2
        
        
        if total_sum == 0:
            return ListNode(0)
            
        dummy = ListNode(0)
        current = dummy
        while total_sum > 0:
            digit = total_sum % 10
            total_sum = total_sum // 10
            
            current.next = ListNode(digit)
            current = current.next
            
        return dummy.next
