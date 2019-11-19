

"""

"""

"""
有理数类
"""

class Rational_01:
    def __init__(self, num, den=1):
        self.num = num
        self.den = den

    def __add__(self, another):
        den = self.den * another.den
        num = (self.num * another.den + self.den * another.num)

        return Rational_01(num, den)

    def __str__(self):

        return '{}/{}'.format(self.num, self.den)

# r1 = Rational_01(5, 3)
# r2 = Rational_01(10, 3)
# print(r1, r2)
# print(r1 + r2)


class Rational_02:

    def __init__(self, num, den=1):

        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        tag = 1
        if num < 0:
            num, tag = -num, -tag
        if den < 0:
            den, tag = -den, -tag
        g = self.gcd(num, den)

        self.__num = (num // g) * tag
        self.__den = den // g

    @staticmethod
    def gcd(num, den):
        if den == 0:
            num, den = den, num
        while num != 0:
            num, den = den % num, num
        return den

    def __add__(self, another):
        den = self.den * another.den
        num = (self.num * another.den + self.den * another.num)

        return Rational_02(num, den)

    def __str__(self):

        return '{}/{}'.format(self.num, self.den)

    @property
    def num(self):

        return self.__num

    @property
    def den(self):

        return self.__den


# r1 = Rational_02(5, 3)
# r2 = Rational_02(10, 3)
# print(r1, r2)
# print(r1 + r2)


"""
栈
"""

class StackError(ValueError):
    pass

class Stack:

    def __init__(self):
        self.__elems = []

    @property
    def is_empty(self):

        return len(self.__elems) == 0

    def top(self):
        if self.is_empty:
            raise StackError('stack is empty')

        return self.__elems[-1]

    def push(self, elem):

        self.__elems.append(elem)

    def pop(self):
        if self.is_empty:
            raise StackError('stack is empty')

        return self.__elems.pop()


"""
队列
"""

class QueueError(ValueError):
    pass

class Queue:

    def __init__(self, init_len=8):
        self.__len = init_len
        self.__elems = [0]*init_len
        self.__head = 0
        self.__num = 0

    @property
    def is_empty(self):
        return self.__num == 0

    def head_elem(self):
        if self.is_empty:
            raise QueueError
        return self.__elems[self.__head]

    def pop(self):
        if self.is_empty:
            raise QueueError
        e = self.__elems[self.__head]
        self.__head = (self.__head + 1) % self.__len
        self.__num -= 1

        return e

    def push(self, e):
        if self.__num == self.__len:
            self.__extend()

        self.__elems[(self.__head + self.__num) % self.__len] = e
        self.__num += 1

    def __extend(self):
        old_len = self.__len
        self.__len *= 2
        new_elems = [0]*self.__len
        for i in range(old_len):
            new_elems[i] = self.__elems[(self.__head + i) % old_len]
        self.__elems, self.__head = new_elems, 0

    def info(self):

        return self.__elems

# que = Queue()
# for i in range(20):
#     que.push(i)
# print(que.pop())
# print(que.info())