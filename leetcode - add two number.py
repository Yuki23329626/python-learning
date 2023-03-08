# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(val=2)
l1.next = ListNode(val=4)
l1.next.next = ListNode(val=3)

l2 = ListNode(val=5)
l2.next = ListNode(val=6)
l2.next.next = ListNode(val=4)

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    add_value = 0
    res = ListNode(val=0)
    res_temp = res

    while True:

        if l1 != None:
            res_temp.val = res_temp.val + l1.val
            l1 = l1.next
        if l2 != None:
            res_temp.val = res_temp.val + l2.val
            l2 = l2.next
        res_temp.val = res_temp.val + add_value
        
        add_value = res_temp.val // 10
        res_temp.val = res_temp.val % 10

        # print("res_temp:", res_temp.val)
        # input()
        
        if (l1 == None and l2 == None) and add_value == 0:
            break
        else:
            res_temp.next = ListNode()
            res_temp = res_temp.next
    return res

res = addTwoNumbers(l1, l2)

while True:
    print(res.val, " ->", end="")
    if res.next == None:
        break
    res = res.next