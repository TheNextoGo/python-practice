#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example:

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#        sum = ListNode(val=0)
        elif l1 == None && l2 == None:
            return None
        elif l1 == None && l2 != None:
            return l2
        elif l1 != None && l2 == None:
            return l1
        else:
            if l1.val + l2.val >= 10:
                l1.next.val += 1
            l1.val = (l1.val + l2.val) % 10
            return l1.next = addTwoNumbers(l1.next,l2.next)
