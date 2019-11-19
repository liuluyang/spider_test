

class Base:
    def func(self):
        print('Base.func')

class A(Base):
    def func(self):
        print('A.func')

    pass

class A2(A):
    pass

class A3(A2):
    pass


# class B(A):
#     def func(self):
#         print('B.func')

class B:
    def func(self):
        print('B.func')

class B2(B):
    pass


class B3(B2):
    pass

class C:
    def func(self):
        print('C.func')

# class Child(A3, B3, C):
#     pass

# class Child(A3, C, B3):
#     pass

class Child(A3, B3):
    pass


# c = Child()
# c.func()
# print(Child.mro())


"""
如果子类继承的父类里面 没有共同继承的父类， 那么按深度优先搜索

如果有共同继承的父类， 留到最后搜索，子类继承的中间有其他类 正常搜索
"""
