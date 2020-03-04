tab = [2, 3, -3, 23, 4, 5, 10, -23, 42, 22, 10]
max = tab[0]

for i in range(len(tab)):
    if tab[i] > max:
        max = tab[i]

print(max)

# ------------------- Zad 2 --------------


class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isdecimal()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):

        for i in exp:
            if self.isOperand(i):
                self.output.append(i)

            elif i == '(':
                self.push(i)

            elif i == ')':
                while((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        while not self.isEmpty():
            self.output.append(self.pop())

        print(''.join(self.output))


exp = "1*(3+5/7^3)-1"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)

# -------------POSTFIX TO INFIX ---------------


def isOperand(x):
    return ((x >= '1' and x <= '9'))


def getInfix(exp):
    s = []
    for i in exp:
        if (isOperand(i)):
            s.insert(0, i)
        else:
            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i + op1 + ")")
    return s[0]


exp = "13573^/+*1-"
print(getInfix(exp.strip()))