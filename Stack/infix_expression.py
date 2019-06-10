from matching import LStack

def calc(a,b,op):
    a = float(a)
    b = float(b)
    if op == '+':
        return a+b
    elif op == '-':
        return b-a
    elif op == '*':
        return a*b
    elif op == '/':
        return b/a

def infix_calculation(expr):
    st_num = LStack()
    st_op = LStack()
    operator = '+-*/()'
    priority = {'+':1,'-':1,'*':2,'/':2,'(':0}

    exp = list(expr.replace(' ',''))
    print(exp)
    for i in exp:
        if i not in operator:
            st_num.push(i)
        else:
            if st_op.is_empty() or i == '(':
                st_op.push(i)
            elif i == ')':
                while st_op.peek() is not '(':
                    op = st_op.pop()
                    a = st_num.pop()
                    b = st_num.pop()
                    result = calc(a,b,op)
                    st_num.push(result)
                st_op.pop()
            elif i in '+-*/':
                if priority[i] > priority[st_op.peek()]:
                    st_op.push(i)
                else:
                    a = st_num.pop()
                    b = st_num.pop()
                    op = st_op.pop()
                    result = calc(a,b,op)
                    st_num.push(result)
                    st_op.push(i)
    while not st_op.is_empty():
        a = st_num.pop()
        b = st_num.pop()
        op = st_op.pop()
        result = calc(a, b, op)
        st_num.push(result)

    return st_num.pop()

expression = '(3 + 2 * 2) * 2 + 5 * 2'
result = infix_calculation(expression)
print(result)


