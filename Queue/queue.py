class Queue:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def peek(self):
        if self.is_empty():
            return False
        return self.elems[0]

    def enqueue(self,e):
        self.elems.append(e)

    def dequeue(self):
        return self.elems.pop(0)




