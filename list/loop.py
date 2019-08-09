class Node:
    def __init__(self,elem, next=None):
        self.elem = elem
        self.next = next

a,b,c,d,e = Node(1),Node(2),Node(3),Node(4),Node(5)
a.next = b
b.next = c
c.next = e
e.next = b

def loop(a):
    a1 = a
    a2 = a
    isloop = False
    while a1.next and a2.next.next:
        a1 = a1.next
        a2 = a2.next.next
        if a1 == a2:
            isloop = True
            break
    if not isloop:
        return False
    a3 = a
    # 推导
    while True:
        if a3 == a1:
            return a1.elem
        a3 = a3.next
        a1 = a1.next

ans = loop(a)
print(ans)