
import datetime
import uuid
import time


"""
异常类、继承、属性、类方法、静态方法、重写、复用、特殊方法、类组合
"""

class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass


class Person:
    __num = 0

    def __init__(self, name, sex, birthday, ident=None):
        if not isinstance(name, str) or sex not in ('女', '男'):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('birthday error:', birthday)
        self.__name = name
        self.__sex = sex
        self.__birthday = birth
        self.__id = ident if ident else self.makeUid()
        Person.__num += 1

    @staticmethod
    def makeUid():

        return str(uuid.uuid1())

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise PersonTypeError('name error', name)
        self.__name = name

    @property
    def sex(self):
        return self.__sex

    @property
    def birthday(self):
        return self.__birthday

    @property
    def age(self):
        return datetime.date.today().year - self.birthday.year

    @classmethod
    def num(cls):
        return cls.__num

    def __str__(self):
        return ' '.join((self.id, self.name, self.sex, str(self.age)))

    def __repr__(self):
        return self.__class__.__name__ + '(%s)'%(
            ','.join((self.id, self.name, self.sex, str(self.age))))


# p1 = Person('xiaohei', '男', (1999, 10, 1))
# p2 = Person('xiaobai', '男', (1999, 10, 2), '11111111112')
#
# print(p1, p2)
# print([p1, p2])


class Student(Person):

    def __init__(self, name, sex, birthday, department):
        super().__init__(name, sex, birthday, self.makeUid())
        self.__department = department      # 院系
        self.__date = datetime.date.today()
        self.__courses = {}                 # 所选课程

    @staticmethod
    def makeUid():

        uid = str(uuid.uuid1())[:8]
        date = str(datetime.date.today()).replace('-', '')
        timestamp = str(time.time()).replace('.', '')

        return '0-{}-{}-{}'.format(date, timestamp, uid)

    @property
    def courses(self):
        return self.__courses

    def set_course(self, name):
        if name in self.courses:
            raise PersonValueError('%s is set'%(name))

        self.__courses[name] = None

    def set_score(self, name, score):
        if name not in self.courses:
            raise PersonValueError('%s is not set'%(name))

        self.__courses[name] = score


# print(datetime.date.today())
# print(time.time())
# stu = Student('xiaohei', '男', (1999, 10, 2), '英语系')
# stu.set_course('基础')
# stu.set_score('基础', 80)
# print(stu.courses)
# print(stu)


class Staff(Person):


    def __init__(self, name, sex, birthday, department):
        super().__init__(name, sex, birthday, self.makeUid())
        self.__department = department      # 院系
        self.__date = datetime.date.today()
        self.__courses = []                 # 所授课程
        self.__position = None              # 职位
        self.__salary = 3000                # 工资

    @staticmethod
    def makeUid():

        uid = str(uuid.uuid1())[:8]
        date = str(datetime.date.today()).replace('-', '')
        timestamp = str(time.time()).replace('.', '')

        return '1-{}-{}-{}'.format(date, timestamp, uid)

    @property
    def salary(self):

        return self.__salary

    @salary.setter
    def salary(self, amount):

        self.__salary = amount

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, name):

        self.__position = name

    def add_course(self, name):
        if name not in self.__courses:
            self.__courses.append(name)

    def del_course(self, name):
        if name in self.__courses:
            self.__courses.remove(name)

    @property
    def courses(self):

        return self.__courses

    def detail(self):

        return {'基本信息':self.__str__(), '院系':self.__department,
                '入职时间':self.__date, '职位':self.position, '工资':self.salary
                }

# sta = Staff('老王', '男', (1978, 10, 1), '计算机系')
# sta.position = '教授'
# sta.salary = 8000
# sta.add_course('c++')
# print(sta, sta.courses)
# print(sta.detail())



"""
扩展：
    学校类、院系类、课程类、职位类
        学校：名称、地址、简介、校长等
        院系：名称、简介、院长、课程等
        课程：名称、简介、课时、授课老师等
        职位：名称、简介、福利等
    学校下面有院系 一对多 互相绑定
    院系下面有课程  一对多 互相绑定
    课程下面有老师  多对多 互相绑定
    老师有所授课程、所属院系、职位
    学生有所选课程、所属院系
    
    注：学生跟老师没有直接关系
"""