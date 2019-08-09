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
            temp.father = self
            temp.left.father = temp

    def insertRight(self, new):
        if self.right == None:
            self.right = BinaryTree(new)
            self.right.father = self
        else:
            temp = BinaryTree(new)
            temp.right = self.right
            self.right = temp
            temp.father = self
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

# no recursion
# def depth_first(tree):
#     res = []
#     s = Stack()
#     while tree:
#         if tree.right:
#             s.push(tree.right)
#         if tree.left:
#             s.push(tree.left)
#
#         res.append(tree.root)
#         tree = s.pop()
#         print(tree)
#
#     return res

pre = []
def pre_order(tree):
    global pre
    if tree is None:
        return

    pre_order(tree.left)
    pre.append(tree.root)
    pre_order(tree.right)

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

# def width_first(tree):
#     q = Queue()
#     res = []
#     while tree:
#         q.enqueue(tree.left)
#         q.enqueue(tree.right)
#
#         res.append(tree.root)
#
#         tree = q.dequeue()
#     return res

pre = ['v','a','c','d','b','e','f']
in_ = ['c','a','d','v','e','b','f']

def recover(pre, in_):
    if not pre:
        return None

    tree = BinaryTree(pre.pop(0))
    children = ''.join(in_).split(tree.root)
    left = [i for i in pre if i in children[0]]
    right = [i for i in pre if i in children[1]]

    tree.left = recover(left, children[0])
    tree.right = recover(right, children[1])

    return tree
new = recover(pre, in_)
print(new)

pre = ['v','a','c','d','b','e','f']
in_ = ['c','a','d','v','e','b','f']
def reConstructBinaryTree(pre, tin):
    if not pre:
        return None

    tree = BinaryTree(pre.pop(0))
    tinL = []
    for i in tin:
        if i != tree.root:
            tinL.append(i)
        else:
            break
    index = len(tinL)
    tinR = [i for i in tin[index+1:]]

    preL = [i for i in pre if i in tinL]
    preR = [i for i in pre if i in tinR]

    tree.left = reConstructBinaryTree(preL, tinL)
    tree.right = reConstructBinaryTree(preR, tinR)

    return tree
new1 = reConstructBinaryTree(pre, in_)
print(new1)
def build_tree():
    tree = BinaryTree('v')
    tree.insertLeft('a')
    tree.insertRight('b')
    tree.left.insertLeft('c')
    tree.left.insertRight('d')
    tree.right.insertLeft('e')
    tree.right.insertRight('f')
    return tree

# tree = build_tree()
# w = width_first(tree)
# print(list(w))
# depth_first(tree)
# pre_order(tree)
# print(depth)
# print(pre)