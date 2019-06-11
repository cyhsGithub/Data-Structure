from binaryTree import BinaryTree,Queue

class PTQueue(Queue):
    def dequeue(self):
        index = 0
        result = self.elems[0].root
        for i,v in enumerate(self.elems):
            if v.root < result:
                index = i
                result = v.root

        return self.elems.pop(index)

class HBinaryTree(BinaryTree):
    def insertLeft(self,new):
        if self.left == None:
            self.left = new
            self.left.father = self
        else:
            temp = new
            temp.left = self.left
            self.left = temp
            temp.father = self
            temp.left.father = temp

    def insertRight(self,new):
        if self.right == None:
            self.right = new
            self.right.father = self
        else:
            temp = new
            temp.right = self.right
            self.right = temp
            temp.father = self
            temp.left.father = temp

def HuffmanTree(weights):
    final = PTQueue()
    for i in weights:
        tree = HBinaryTree(i)
        final.enqueue(tree)

    while len(final.elems) > 1:
        t1 = final.dequeue()
        t2 = final.dequeue()
        t = HBinaryTree(t1.root + t2.root)
        t.insertLeft(t1)
        t.insertRight(t2)
        final.enqueue(t)

    return final.dequeue()

def width_first(tree):
    qu = Queue()
    qu.enqueue(tree)

    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue

        qu.enqueue(t.left)
        qu.enqueue(t.right)
        yield t.root

weights = [60,45,13,69,14,5,3]
hTree = HuffmanTree(weights)
tree = width_first(hTree)
print(list(tree))