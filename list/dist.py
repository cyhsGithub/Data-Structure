#使链表奇数在前偶数在后，相对位置不变
class Node:
    def __init__(self,elem, next=None):
        self.elem = elem
        self.next = next

a,b,c,d,e = Node(1),Node(2),Node(3),Node(4),Node(5)
a.next = b
b.next = c
c.next = d

def dist(a):
    last_odd = None
    first_even = None

    head = a
    last = None
    while head:
        if head.elem % 2 == 0:
            if not first_even:
                first_even = head
            last = head
            head = head.next
            continue
        if first_even:
            last.next = head.next
            if not last_odd:
                t = head
                head = head.next
                t.next = first_even
                last_odd = t
            else:
                t = head
                head = head.next
                t.next = first_even
                last_odd.next = t
                last_odd = t
            continue
        last_odd = head
        head = head.next
    return a

res = dist(a)
print(res.elem, res.next.elem, res.next.next.elem, res.next.next.next.elem)






