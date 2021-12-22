from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		ori = ListNode(0)
		res = ori
		remainder = 0
		while l1 or l2:
			calc = remainder
			if l1:
				calc += l1.val
				l1 = l1.next
			if l2:
				calc += l2.val
				l2 = l2.next
			if calc >= 10:
				remainder = 1
				res.val = calc % 10
			else:
				remainder = 0
				res.val = calc
			if l1 or l2:
				res.next = ListNode(0)
				res = res.next
		return ori
l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
tmp = addTwoNumbers(l1,l2)
while tmp:
	print(tmp.val)
	tmp = tmp.next