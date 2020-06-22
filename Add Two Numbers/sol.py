class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = current = ListNode()
        carry = 0
        while l1 or l2:
            total = carry
            carry = 0

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            if total >= 10:
                carry = 1
                total%=10
            
            current.next = ListNode(total)
            current = current.next
        if carry: current.next = ListNode(1)
        return head.next