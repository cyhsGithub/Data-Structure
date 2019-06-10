import copy
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

class BinaryTree:

    def __init__(self, root):
        self.root = root
        self.father = None
        self.left = None
        self.right = None

    def insertLeft(self, new):
        if self.left == None:
            self.left = BinaryTree(new)
            self.left.father = self
        else:
            temp = BinaryTree(new)
            temp.left = self.left
            self.left = temp
            temp.father = self.left
            temp.left.father = temp

    def insertRight(self, new):
        if self.right == None:
            self.right = BinaryTree(new)
            self.right.father = self
        else:
            temp = BinaryTree(new)
            temp.right = self.right
            self.right = temp
            temp.father = self.right
            temp.left.father = temp

    def clone(self):
        return copy.deepcopy(self)

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRoot(self, root):
        self.root = root

    def getRoot(self):
        return self.root

depth = []
def depth_first(tree):
    global depth
    if tree is None:
        return

    depth.append(tree.root)
    depth_first(tree.left)
    depth_first(tree.right)

pre = []
def pre_order(tree):
    global width
    if tree is None:
        return

    pre_order(tree.left)
    pre.append(tree.root)
    pre_order(tree.right)

def width_first(tree):
    qu = Queue()
    qu.enqueue(tree)
    print(qu.is_empty())

    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue

        qu.enqueue(t.left)
        qu.enqueue(t.right)
        yield t.root

def build_tree():
    tree = BinaryTree('v')
    tree.insertLeft('a')
    tree.insertRight('b')
    tree.left.insertLeft('c')
    tree.left.insertRight('d')
    tree.right.insertLeft('e')
    tree.right.insertRight('f')
    return tree

tree = build_tree()
w = width_first(tree)
print(list(w))
# depth_first(tree)
# pre_order(tree)
# print(depth)
# print(pre)