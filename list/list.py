import copy

class ListIndexOutofRange(Exception):
    def __init__(self,info):
        self.info = info

class Node:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

class LinkedList:
    def __init__(self):
        self.head = None
        self.num = 0

    def __len__(self):
        return self.num

    def is_empty(self):
        return self.head is None

    def append(self,elem):
        if self.head == None:
            self.head = Node(elem)
            self.num += 1
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(elem)
        self.num += 1

    def insert(self,elem,position):
        temp = self.head
        try:
            if position == 1:
                if temp is None:
                    raise ListIndexOutofRange("Exception: indexOutofRange")
            else:
                for i in range(position - 2):
                    if temp is None:
                        raise ListIndexOutofRange("Exception: indexOutofRange")
                    temp = temp.next

            t = temp.next
            temp.next = Node(elem, t)
            self.num += 1
        except ListIndexOutofRange as e:
            print(e.info)

    def delete(self,element = None, position = None):
        temp = self.head

        if element:
            if temp.elem == element:
                self.head = self.head.next
                return

            while temp.next:
                if temp.next.elem == element:
                    temp.next = temp.next.next
                    self.num -= 1
                else:
                    temp = temp.next
        elif position:
            if position == 1:
                self.head = self.head.next
                return

            for i in range(position-2):
                temp = temp.next

            temp.next = temp.next.next

    def locate(self,position):
        temp = self.head

        try:
            if position <= 0:
                raise ListIndexOutofRange("Exception: indexOutofRange")
            for i in range(position-1):
                if temp:
                    temp = temp.next
                else:
                    raise ListIndexOutofRange("Exception: indexOutofRange")

            return temp.elem
        except ListIndexOutofRange as e:
            # print(e.info)
            return e.info

    def bubble_sort(self):
        if self.head == None:
            return

        t = self.head.next
        while t is not None:
            x = t.elem
            p = self.head
            while p is not t and p.elem <= x:
                p = p.next
            while p is not t:
                p.elem,x = x,p.elem
                p = p.next
            t.elem = x
            t = t.next

    def deep_copy(self):
        out = copy.deepcopy(self)
        return out

    def reverse(self):
        p = None
        while self.head:
            q = self.head
            self.head = q.next
            q.next = p
            p = q
        self.head = p

    def rev(self):
        t = self.head
        while t:
            p = t
            t = t.next
            p.next = None
            t.next = p
        return

    def test(self):
        t = self.head
        self.head = self.head.next
        return


    def printList(self):
        temp = self.head
        list = []
        while temp:
            list.append(temp.elem)
            temp = temp.next
        print(list)

class LCList:
    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear is None

    def prepend(self,elem):
        p = Node(elem)

        if self.rear == None:
            p.next = p
            self.rear = p
        else:
            p.next = self.rear.next
            self.rear.next = p

    def append(self,elem):
        self.prepend(elem)
        self.rear = self.rear.next

    def pop(self):
        try:
            if self.rear == None:
                raise ListIndexOutofRange("in pop of CLList")
            p = self.rear.elem
            q = self.rear
            m = self.rear.next
            if q == m:
                self.rear = None
                return p

            while q.next is not self.rear:
                q = q.next

            q.next = m
            self.rear = q
            return p
        except ListIndexOutofRange as e:
            print(e.info)

    def printList(self):
        if self.is_empty():
            return False
        p = self.rear.next
        while True:
            print(p.elem,end=' ')
            if p == self.rear:
                print('\n')
                break
            p = p.next

#
# l = LCList()
# l.append(1)
# l.append(2)
# l.append(3)
# n = l.pop()
# print(n)
# l.printList()
