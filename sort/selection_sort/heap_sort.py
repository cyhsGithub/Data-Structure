#O(nlogn),交换n次，每次交换后的调整是logn
#堆 == 完全二叉树，
#对于深度为K的，有n个结点的二叉树，当且仅当其每一个结点
# 都与深度为K的满二叉树中编号从1至n的结点一一对应时称之为完全二叉树
def heap_sort(li):
    initial_heap(li)
    pos = len(li)-1
    for i in range(len(li)):
        if pos == 0:
            break
        li[0],li[pos] = li[pos],li[0]
        pos -= 1
        heap_adjust(li,pos)


def initial_heap(li):
    for i in range(len(li)-1, -1, -1):
        while True:
            if 2 * i + 1 < len(li):
                #没有右结点
                if 2*i+2 == len(li):
                    if li[2*i+1] > li[i]:
                        li[2 * i + 1], li[i] = li[i], li[2 * i + 1]
                    break
                #左右孩子中最大的如果比父亲大则交换，然后调整交换后的子树
                elif li[2*i+1] >= li[2*i+2] and li[2*i+1] > li[i]:
                    li[2*i+1],li[i] = li[i],li[2*i+1]
                    i = 2 * i + 1
                elif li[2*i+2] > li[2*i+1] and li[2*i+2] > li[i]:
                    li[2*i+2], li[i] = li[i], li[2*i+2]
                    i = 2 * i + 2
                else:
                    break
            else:
                break

def heap_adjust(li,pos):
    i = 0
    while True:
        if 2*i+1 <= pos:
            if 2*i+2 == len(li):
                if li[2*i+1] > li[i]:
                    li[2 * i + 1], li[i] = li[i], li[2 * i + 1]
                break
            elif li[2 * i + 1] >= li[2 * i + 2] and li[2 * i + 1] > li[i]:
                li[2 * i + 1], li[i] = li[i], li[2 * i + 1]
                i = 2 * i + 1
            elif li[2 * i + 2] > li[2 * i + 1] and li[2 * i + 2] > li[i]:
                li[2 * i + 2], li[i] = li[i], li[2 * i + 2]
                i = 2 * i + 2
            else:
                break
        else:
            break



li = [1, 5, 8, 0, 123, 22, 1, 54, 7, 99, 300, 222]
heap_sort(li)
print(li)