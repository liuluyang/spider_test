


class Person:

    instance = None
    # print('Person')

    def __init__(self, name):
        """
        初始化函数
        没有返回值
        :param name:
        """
        print('__init__')
        self.name = name

    def __call__(self, *args, **kwargs):
        """
        让实例化对象可以像函数一样调用
        :param args:
        :param kwargs:
        :return:
        """
        print('__call__', args, kwargs)

    def __new__(cls, *args, **kwargs):
        """
        Person的构造函数
        创建空的实例对象
        返回实例对象
        :param args:
        :param kwargs:
        :return:
        """
        print('__new__', cls, args, kwargs)
        if not cls.instance:
            obj_new = object.__new__(cls)
            cls.instance = obj_new
        return cls.instance

# p = Person('小白')
# p2 = Person('小黑')
# print(p, p.__dict__)
# print(p2, p2.__dict__)



class TypeBase(type):

    def __init__(cls, what, bases=None, dict=None):
        """
        初始化函数
        没有返回值
        :param what:类名
        :param bases:父类
        :param dict:类的属性字典
        """
        cls.NN = 111111
        cls.__instance = None
        print(cls, what, bases, dict)

    def __new__(cls, *args, **kwargs):
        """
        type的构造函数
        创建空的类
        返回实例对象（类）
        :param args:
        :param kwargs:
        :return:
        """
        print(cls, args, kwargs)
        # if args[0] != 'F':
        #     raise ValueError

        return type.__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        类实例化的时候会调用这个方法
        :param args:
        :param kwargs:
        :return:
        """
        print(self, args, kwargs)
        if not self.__instance:
            self.__instance = super().__call__(*args, **kwargs)

        return self.__instance

class B:
    pass

class F(B, metaclass=TypeBase):

    N = 1

    def __init__(self, name):
        self.name = name

    def w(self):
        print('w')
        pass

class Child(F):

    pass

# print(F.N, F.NN, F.__dict__)
# f = F('xx')
# #
# print(f, f.name)
# f.w()
print('#'*20)

"""
1. 类里修改__new__实现单例模式
2. 元类里通过重写__call__/__init__实现单例模式
"""
# c1 = Child('xx')
# c2 = Child('yy')
#
# print(c1 is c2)
# print(c1.__dict__)
# print(c2.__dict__)