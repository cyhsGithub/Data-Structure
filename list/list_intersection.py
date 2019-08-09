class Node:
    def __init__(self,elem, next=None):
        self.elem = elem
        self.next = next

a,b,c,d,e = Node(1),Node(2),Node(3),Node(4),Node(5)
a.next = b
b.next = c
c.next = e
d.next = e

def intersection(a, b):
    a1 = a
    b1 = b
    is_intersection = False
    len_a = 1
    len_b = 1
    while a1.next is not None:
        a1 = a1.next
        len_a += 1

    while b1.next is not None:
        b1 = b1.next
        len_b += 1

    if a1.elem == b1.elem:
        is_intersection = True

    if not is_intersection:
        return False

    start = 0
    if len_a > len_b:
        start = len_a - len_b
        for i in range(start):
            a = a.next
    else:
        start = len_b - len_a
        for i in range(start):
            b = b.next

    pos = start
    while True:
        if a == b:
            return pos
        a = a.next
        b = b.next
        pos += 1
res = intersection(a,d)
print(res)

