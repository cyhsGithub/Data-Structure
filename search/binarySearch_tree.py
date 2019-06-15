#平均O(logn)，最坏O(n)(建树最不平衡的情况)
#平衡二叉树，AVL算法，parent结点的平衡因子为右孩子高度减去左孩子高度，若等于2
#则需要旋转更新
import random
def operation():
    print("Found")

class BinarySearchTree:

    def __init__(self, root = None):
        self.root = root
        self.father = None
        self.left = None
        self.right = None

    def insert(self, new):
        t = self
        if not t.root:
            t.root = new
            return
        while True:
            if new > t.root:
                if t.right is None:
                    t.right = BinarySearchTree(new)
                    return
                t = t.right
            elif new < t.root:
                if t.left is None:
                    t.left = BinarySearchTree(new)
                    return
                t = t.left
            else:
                return

    def build(self,li):
        random.shuffle(li)
        for i in li:
            self.insert(i)

    def search(self,key):
        t = self
        time = 0
        while t:
            time += 1
            if key == t.root:
                operation()
                print(time)
                return
            elif key > t.root:
                t = t.right
            else:
                t = t.left

        return "Not Found"



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

d = []
def in_order(tree):
    global d
    if not tree:
        return

    in_order(tree.left)
    d.append(tree.root)
    in_order(tree.right)

li = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
tree = BinarySearchTree()
tree.build(li)
tree.search(300)
in_order(tree)
print(d)
