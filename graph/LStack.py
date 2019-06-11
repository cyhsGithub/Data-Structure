class Node():
    def __init__(self,elem=None, next=None):
        self.elem = elem
        self.next = next

class LStack():
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self,elem):
        self.top = Node(elem, self.top)

    def pop(self):
        try:
            if self.top == None:
                raise ListIndexOutofRange("in pop")
            p = self.top
            self.top = p.next
            return p.elem
        except ListIndexOutofRange as e:
            print(e.info)

    def peek(self):
        try:
            if self.top == None:
                raise ListIndexOutofRange("in peak")
            return self.top.elem
        except ListIndexOutofRange as e:
            print(e.info)