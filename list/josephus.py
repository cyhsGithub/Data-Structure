from list import LCList

def josephus_A(n,k,m):
    '''
    假设有n个人围坐一圈，现要求从第k个人开始报数，报到第m个数的人退出。
    然后从下一个人开始继续报数并按同样的规则退出，直至所有人退出，要求按顺序输出各出列人的编号
    :return:
    '''
    people = list(range(1,n+1))

    result = []
    i= k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                result.append(people[i])
                people[i] = 0
            i = (i+1) % n

    print(result)
    return

josephus_A(10, 5, 6)

class Josephus(LCList):
    def turn(self,m):
        for i in range(m):
            self.rear = self.rear.next

    def __init__(self):
        super().__init__()
        self.result = []

    def do(self,n,k,m):
        for i in range(n):
            self.append(i + 1)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m)
            self.result.append(self.pop())

        print(self.result)

j = Josephus()
j.do(10,5,6)