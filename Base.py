"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: test.py
@time: 2020/8/17 14:39
@desc:
==============================
"""

import types
from functools import wraps
import time
import pymysql
import copy
import gc
import threading
import requests
import flask
import queue
import queue
from multiprocessing import Process, Queue, Manager, Pool
import greenlet
from gevent import monkey
import gevent


def required_type(t):
    def required(fn):
        def wrapper(*args, **kwargs):
            for i in args:
                if not isinstance(i, t):
                    print("Error:参数类型必须是：", t)
                    break
            else:
                return fn(*args, **kwargs)

        return wrapper

    return required


@required_type(float)
def add(x, y):
    return x + y


def is_value(name):
    def is_admin(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if name == "root":
                func(*args, **kwargs)
            else:
                print("用户不是admin/root用户，没有权限进行操作")

        return wrapper

    return is_admin


user_list = ["admin", "root", "visitor "]


def is_key(name):
    def is_login(func):
        def wrapper(*args, **kwargs):
            if name in user_list:
                func(*args, **kwargs)
            else:
                print("用户未登录，请先登录")

        return wrapper

    return is_login


def count_time(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print("李彦路和如花运动时间是：{}秒".format(int(end - start)))

    return wrapper


@count_time
@is_key("root")
@is_value("root")
def add_student(name):
    time.sleep(2)
    print("陪酒女—————{}".format(name))


class MyClass(object):
    def __init__(self, name):
        self.name = name
        print("这个类的初始化函数参数传递的是：{}".format(self.name))

    def __new__(cls, *args, **kwargs):
        print("这是一个重写的new方法")
        return super().__new__(cls)             # 调返回一个对象，执行init的方法，否则不执行，可以继承父类的
        # return object.__new__(cls)            # 第二种方法继承父类new方法


# 单例模式


class MyTest(object):
    instance = None                                 # 设置一个类属性，用来记录该类有无创建实例对象

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)      # 如果为空创建个对象，通过父类的new方法
            return cls.instance
        else:
            return cls.instance


class MyTest1(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print("str被触发")
        return "haha"                           # print打印的是__str__方法返回的内容,返回的必须是字符串

    def __repr__(self):
        print("触发repr")
        return "haha"

    def __call__(self, *args, **kwargs):
        print("call方法被调用")


# 装饰器定义单例模式

def demo(cls):
    instance = {}                                   # 把实例对象先复为空值

    @wraps(cls)                                      # 通过wraps装饰器使.__doc__文档内容不发生变化
    def is_object(*args, **kwargs):
        if cls not in instance:                     # 当实例为空是进行下面操作
            instance[cls] = cls(*args, **kwargs)  # 创建实例将这个实例保存到这个字典中
        return instance[cls]

    return is_object


@demo
class A(object):

    def __int__(self):
        self.a = "1"
        self.b = "2"


class Demo:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):                # 类能不能被当成函数调用，取决于call方法，类函数就是调用这个方法
        print("被装饰器装饰的功能")
        self.fn()
        print("执行功能函数")


@Demo
def test_01():
    print("被装饰的函数！")


# with open("test.txt", "w", encoding="utf8") as f:
# f.write("hello world")


class MyOpen(object):           # 上下文管理器

    def __init__(self, filename, method, encoding="utf8"):
        self.filename = filename
        self.method = method
        self.encoding = encoding

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("上下文管理器关闭文件的方法")
        # 可通过(exc_type("异常类型"), exc_val("异常值"), exc_tb("异常对象"))输出异常日志
        self.f.close()

    def __enter__(self):
        print("上下文管理器返回数据的方法")
        self.f = open(self.filename, self.method, encoding=self.encoding)
        return self.f


# with MyOpen("test1.txt", "a") as f:
#     print(f.write("\n秦皇汉武，威震寰宇"))

# 多态


class Base(object):
    __name = "李刚"

    def run(self):
        print("原始技能————走路")


class Cat(Base):
    def run(self):
        print("猫会爬树")


class Dog(Base):
    def run(self):
        print("狗跑的很快")


class Tortoise(Base):
    def run(self):
        print("乌龟爬得很慢")


def two_run(fn):                # 传入类，调用不同的run方法
    fn.run()


class Open:
    __slots__ = ["name"]  # __slots__  :限制属性，省内存占用
    # 这个类只能添加一个name的属性，实例化调用，可以限制对象属性指定类对象所能绑定的属性
    # 定义了这个slots，这个对象就没有了 dict这个属性了。


class Person(object):
    """
    在子类中是不能继承私有属性和方法的，
    但是私有属性和方法可以在同一个类中被调用
    """
    name = "李毅"
    __sex = '女'

    def __run(self):
        print('base class is running')

    def running(self):
        self.__run()


class Student(Person):

    def greet(self):
        self.__run()


class Person(object):
    def __init__(self, age):
        self.__age = age

    def age(self):                      # 通过这层包装，继承的子类通过访问此方法来访问私有属性
        return self.__age

    def __set_age(self, age):           # 这是私有方法，子类也无法直接访问。

        if not isinstance(age, int):
            raise ValueError('score must be an integer!')
        if age < 0 or age > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = age               # 给私有属性赋值，传递新值

    def set_age(self, age):             # 子类的实例可以正常调用此方法
        self.__set_age(age)


class Student(Person):
    def dis(self):
        print(self.age())


class Monkey(object):           # 类名，括号可写可不写
    age = 18                    # 类也是一个数据类型，本身并不占用内存，实例化才华占用内存
    name = "A"                  # 属性，静态属性

    def run(self):  # 类方法，行为
        print("第一个类方法")


class Student(object):
    name = 'Student'


def add():
    return 1 + 2


m = Monkey()
hasattr(m, "age")

type(add) == types.FunctionType

h = Student()                       # 判断一个对象是否是该类型本身，或者位于该类型的父级上
isinstance(h, Student)
dir(h)


class Tes:
    age = None


getattr(Tes, "age")              # 获取属性
setattr(Tes, "age", 18)          # 给属性赋新值
getattr(Tes, "age")             # 获取属性
hasattr(Tes, "age")             # 判断对象是否包含属性


class DataSet(object):
    @property
    def method_with(self):              # 含有@property
        return 15

    def method_without(self):           # 不含@property
        return 15


class DataSet(object):
    def __init__(self):
        self._images = 1
        self._labels = 2                # 定义属性的名称

    @property
    def images(self):                   # 方法加入@property后，方法可以跟访问属性一样去访问，且这个属性是可读的不能更改值
        return self._images

    @property
    def labels(self):
        return self._labels


class Exam(object):
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, val):
        if val < 0:
            self.__score = 0
        elif val > 100:
            self.__score = 100
        else:
            self.__score = val
            return self.__score


class Exam1(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val


class Tess:
    def __getattr__(self, item):                    # 未查到属性返回一个固定值或者报一个异常
        print("查找属性时未查到，出现attr_error时触发该方法，如果访问不存在的属性，不会报错，返回None")
        super().__getattribute__(item)              # 通过父类的查找属性方法来触发异常

    def __getattribute__(self, item):               # 先执行该方法，getattr是兜底最后查找
        print("查找属性时第一时间触发该方法去查找")

    def __setattr__(self, key, value):
        print("设置属性的时候，触发该方法")
        super().__setattr__(key, value)             # 通过父类的方法把数值生成成功，也可以进行干扰(不让随意设置更改)

    def __delattr__(self, item):
        print("删除属性的时候调用该方法")
        super().__delattr__(item)                   # 继承父类执行删除操作


# 连接数据库的上下文管理器

class ConnectSql:
    def __init__(self, sql_data):
        self.con = pymysql.connect(**sql_data)              # 建立连接服务
        self.cursor = self.con.cursor()                     # 设置游标

    def __enter__(self):
        return self.cursor  # 先调用游标返回

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()


data = {
    "host": "192.168.0.24", "user": "test_cps_user", "password": "test_cps_userpass123456",
    "database": "cps", "port": 3306, "charset": "utf8"}


# with ConnectSql(DA_data)as cur:
#     cur.execute("select * FROM activity where id =1")
#     print(cur.fetchone())


class AS:                                   # 只要类中出现该方法任意一个，此类就是描述器类
    def __set__(self, instance, value):     # 未设置该方法数值时，访问或访问其他两个方法返回None，
        print("设置属性时触发——set")
        self.value = value

    def __get__(self, instance, owner):
        print("获取属性时触发——get")
        return self.value  # 返回设置的属性值

    def __delete__(self, instance):
        print("删除属性时触发--delete")
        self.value = None


class OB:
    sf = AS()


# 描述器定义ORM模型


class CharFiled:
    def __init__(self, max_length=20):
        self.max_length = max_length

    def __get__(self, instance, owner):

        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_length:
                self.value = value
            else:
                print("输出字符长度超过{}限制".format(self.max_length))

        else:
            print("typeerror错误！")

    def __delete__(self, instance):
        self.value = None


class IntFiled:
    def __init__(self, max_length=20, not_null=False):
        self.max_length = max_length
        self.not_null = not_null

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value

        else:
            print("typeerror错误！")

    def __delete__(self, instance):
        self.value = None


class Create1:
    id = IntFiled(max_length=20)
    name = CharFiled(max_length=20)
    age = IntFiled(max_length=20)


class L:
    pass


def fun(self):                  # 外部定义方法，需要带self参数
    print("self")
    # 元类创建类，传三个参数，name:字符串（类名）,bases:元组（继承的父类名，可以为空），attr_dict（属性和方法）


Test = type("Test", (object,), {"name": 18, "sex": fun})
t = Test()


class MyClass(type):            # 自定义元类必须继承元类
    """
    'type'实际上是一个类，就像'str'和'int'一样,所以你可以从type继承
    __new__ 是在__init__之前被调用的特殊方法,而__init__只是用来将传入的参数初始化给对象,__new__是用来创建对象并返回之的方法
    你也可以在__init__中做些事情,可以改写__call__特殊方法
    """

    def __new__(cls, class_name, class_bar, class_attr, *args, **kwargs):
        # print("元类的new————方法")
        # return super().__new__(cls, class_name, class_bar, class_attr )
        pass


class Op(metaclass=MyClass):  # metaclass指定引用元类，不指定默认type元类
    miss = 12


# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(class_name, class_parents, class_attr):
    """ 返回一个类对象，将属性都转为大写形式 """
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    __metaclass__ = upper_attr  # 这会作用到这个模块中的所有类
    # 通过'type'来做类对象的创建
    return type(class_name, class_parents, uppercase_attr)


class Fo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


class ClassType(type):                  # 自定义元类必须继承元类

    def __new__(mcs, class_name, class_bar, class_attr, *args, **kwargs):
        # print("元类的new————方法")
        for k, v in list(class_attr.items()):
            class_attr.pop(k)
            class_attr[k.upper()] = v

        return type.__new__(mcs, class_name, class_bar, class_attr)


class Cps(metaclass=ClassType):  # metaclass指定引用元类，不指定默认type元类
    name = '李浩'
    age = 12
    sex = '女'


class UpperAttrMetaclass(type):
    def __new__(mcs, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(mcs, name, bases, uppercase_attr)


class UpperAttrMetaclass(type):
    def __new__(mcs, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super().__new__(mcs, name, bases, uppercase_attr)


# 利用元类创ORM建模型


class Field(object):
    # 创建自定义字段属性父类
    pass


class CharField(Field):
    # 自定义字符型字段属性

    def __init__(self, length=20):
        self.max_length = length
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_length:
                self.value = value
            else:
                print("输出字符长度超过{}限制".format(self.max_length))
        else:
            print("typeerror错误！")

    def __delete__(self, instance):
        self.value = None


class IntFiled(Field):
    # 自定义整型字段属性

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            print("typeerror错误！")

    def __delete__(self, instance):
        self.value = None


class BoolFiled(Field):
    # 自定义描述器布尔值类型

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            print("typeerror错误！")

    def __delete__(self, instance):
        self.value = None


class OrmClass(type):
    # 创建跟数据表对应关系映射的元类

    def __new__(mcs, name, base, _dict, *args, **kwargs):
        if name == "BaseClass":
            return super().__new__(mcs, name, base, _dict)
        else:
            table_name = name.lower()               # 类名转换成小写对应数据表名称
            fields = {}                             # 定义空字典存储_dict属性，过滤一下自带的双下划线的属性
            for key, value in list(_dict.items()):  # 提取数据表字段做映射，属性字段存储在_dict里面
                if isinstance(value, Field):        # 判断value的值是不是定义的元类类型，key类型固定判断value
                    fields[key] = value             # 是定义的类型就把他加入到空字典中
            _dict["t_name"] = table_name            # 把表名和创建过滤的字段添加到_dict 属性里面形成映射关系
            _dict["field"] = fields                 # 创建的对应的映射关系都通过_dict 返回给模型类

            return super().__new__(mcs, name, base, _dict)


class BaseClass(metaclass=OrmClass):            # 创建模型类的父类重新给init方法，然后父类指定元类，子类直接继承
    def __init__(self, **kwargs):               # 多个模型类都继承父类，不能写死，用不定长参数传递关键字
        for k, v in list(kwargs.items()):       # 遍历出传递字典的键和值
            setattr(self, k, v)                 # 通过内置函数给属性设置值,通过init设置属性是实例属性

    def save(self):                                         # 定义保存到数据库的方法
        t_name = self.t_name                                # 获取表名
        fields = self.field                                 # 创建一个字典用来存储字段的键值对
        field_list = {}
        for field in fields.keys():                         # 遍历出字段所有的键，通过键去查找值
            field_list[field] = getattr(self, field)        # 通过内置函数获取值
        # 生成sql语句，字典转换成元组
        sql = "INSERT INTO {0} key{1} value{2};".format(t_name, tuple(field_list.keys()), tuple(field_list.values()))
        print(sql)


class User(BaseClass):
    # 指定元类，创建用户模型
    username = CharField()
    pwd = CharField()
    age = IntFiled()
    live = BoolFiled()


class Order(BaseClass):
    # 订单模型类
    Id = IntFiled()
    order_num = IntFiled()
    money = IntFiled()


u = User(username="小明", pwd="123", age=17, live=True)

r = gc.get_threshold()              # 传入对象到达的数量开始扫描，1代触发扫描条件，二代出发扫描的条件 （默认700.10.10）


def fun1():
    for i in range(6):
        time.sleep(1)
        print("正在执行任务1{}".format(threading.current_thread()))  # 返回当前正在执行的线程,获取线程对象


def fun2():
    for j in range(5):
        time.sleep(1)
        print("正在执行任务2{}".format(threading.current_thread()))


def main():
    t = threading.Thread(target=fun1)  # 创建线程对象，fun 线程执行的任务，一个任务就是一个函数
    h = threading.Thread(target=fun2, name="线程2")  # 创建一个线程执行任务2，返回一个线程对象，name属性设置线程名称
    s_time = time.time()
    print(t.is_alive())              # 判断线程是否执行，返回True和False
    t.start()                        # 开始执行线程1，start是通过run方法执行任务，可以通过重写run方法把任务写在run方法
    t.setName("线程1")                # 设置线程名称
    print(t.getName())               # 获取线程名称
    h.start()                        # 开始执行线程2
    print(threading.enumerate())     # 获取当前所有活动的线程，返回列表
    print(threading.active_count())  # 统计当前活动的线程，计数，返回一个int，主线程+子线程
    print(h.name)                    # 通过属性值获取线程2名称
    t.join()
    h.join()                         # 子线程执行完毕，在执行主线程。参数是时间根据时间设置主线程等待多长时间执行，不写默认执行完
    end_time = time.time()
    print("耗时{}".format(end_time - s_time))


class Threads(threading.Thread):      # 继承threading类的Thread方法

    def __init__(self, url):
        self.url = url
        super().__init__()   # 重写子类的init方法必须继承父类的init方法

    def run(self):              # 重写run方法执行任务
        r = requests.get("https://www.baidu.com")
        print("请求状态码{}".format(threading.active_count(), threading.current_thread(), r.status_code))


count = 0


class Cps(threading.Thread):
    def run(self):
        global count
        for i in range(10):
            requests.get("http://www.baidu.com")
            count += 1
        print("线程{}发送{}请求".format(self.name, i+1))    # self.name 指的是传入线程名字，取得默认值，i取值范围0-9打印是9所以要+1


def ma():
    s_time = time.time()
    th = [Cps() for j in range(10)]    # 通过列表推导式创建10个子线程
    for i in th:                       # 循环调用子线程10次
        i.start()
    for j in th:                       # 循环调用子线程10次，等待主线程执行完毕
        j.join()
    e_time = time.time()
    print("平均耗时：{}".format((e_time - s_time) / count))
    print("运行{}".format(count))


n = 0
meta = threading.Lock()   # 创建所对象，当前数据修改完以后释放，修改期间其他线程不能修改
meta_1 = threading.Lock()


def fun11():
    global n
    for i in range(1000000):
        meta.acquire()        # 上锁
        meta_1.acquire()
        print("1")
        n += 1
        meta_1.release()
        meta.release()        # 释放锁
    print("线程组1修改完a的值{}".format(n))


def fun22():
    global n
    for j in range(1000000):
        meta_1.acquire()
        meta.acquire()
        print("2")
        n += 1
        meta.release()
        meta_1.release()
    print("线程组2修改后a的值{}".format(n))


def mx():
    t_time = time.time()
    ti = threading.Thread(target=fun11())
    to = threading.Thread(target=fun22())
    ti.start()
    ti.join()
    to.start()
    to.join()
    e_time = time.time()
    print("运行时间{}".format(e_time - t_time))


"""
q.put(1)                    # 往队列插入数据，如果block为true，timeout为等待，如果队列满了一直都塞，直到超时
q.put(123)
# q.put(11, block=False)     # block为false不等待，队列满了直接报错
q.put_nowait(12)             # 等同put的block=false
q.join()                     # 判断队列任务是否执行完毕，执行完毕才会向下执行，否则在此堵塞
q.get()                      # 从队列获取数据，先入先出取出队列第一个数值,block为true，timeout为等待，如果队列满了一直都塞，直到超时
q.get(block=False)           # block为false不等待，队列满了直接报错
q.get_nowait()               # 等同block=False，不等待
q.full()                     # 判断队列是否满了
q.qsize()                    # 返回队列的消息数量
q.empty()                    # 判断队列是否为空，true为空false不为空

q.task_done()               # 队列执行一次任务，发送一次消息
"""
q = queue.Queue(6)          # 设置队列的长度，不设置或者负数表示不限
# for i in range(6):          # 先入先出
#     q.put(i)

# while not q.empty():
#     print(q.get())

q1 = queue.LifoQueue()      # 后入先出

# for i in range(5):
#     q1.put(i)

# while not q1.empty():
#     print(q1.get())

q2 = queue.PriorityQueue()     # 优先级队列
q2.put((3, "hello_java"))     # 传入一个元组，第一个参数是优先级，第二个是值，优先级越低越先取出
q2.put((1, "hello_python"))
q2.get()

# 多线程运用优先级队列

q3 = queue.PriorityQueue()

q3.put((3, 'level 3 job'))
q3.put((10, 'level 10 job'))
q3.put((1, 'level 1 job'))

# 消费商品，生产商品
a = queue.Queue()


class Production(threading.Thread):
    def run(self):
        count = 0
        while True:
            if a.qsize() < 50:
                for k in range(200):
                    count += 1
                    glo = "第{}个商品".format(count)
                    a.put(glo)
                    print("生产商品{}".format(glo))
                time.sleep(2)


class Consume(threading.Thread):
    def run(self):
        while True:
            if a.qsize() > 10:
                for l in range(3):
                    print("消费商品{}".format(a.get()))
                time.sleep(0.2)


pk = Production()
c = Consume()

# 多线程执行多任务，实行真正的并行，线程只能并发


"""
p = Process()               # 创建进程
p.start()                   # 运行子进程，它调用的run方法
p.is_alive()                # 判断子进程是否还活着
p.join()                    # 子进程等待时间
p.run()                     # 启动子进程
p.terminate()               # 不管任务是否完成，立即终止子进程
s = Queue()                 # 进程下的特用的队列，处理多进程之间的共享数据
# process创建进程长用参数:{name  # 子进程的名称,pid   # 进程id号}
"""

g = 1


def ws(q):
    while q.qsize() > 0:
        global g
        url = q.get()
        requests.get(url)
        print("任务1正在运行{}".format(g))
        g += 1


def ed(q):
    while q.qsize() > 0:
        global g
        url = q.get()
        requests.get(url)
        print("任务2正在运行{}".format(g))
        g += 1


q = queue.Queue()    # 线程队列（只能在一个进程使用）
for i in range(50):
    q.put("http://www.baidu.com")

def main():
    ts = time.time()
    so = threading.Thread(target=les)
    so1 = threading.Thread(target=les)
    so2 = threading.Thread(target=les)
    so.start()
    so1.start()
    so2.start()
    so.join()
    so1.join()
    so2.join()
    es = time.time()
    print("执行时间{}".format(es - ts))


def les():
    url = q.get()
    requests.post(url=url)


def wc():
    ts = time.time()
    q3 = Manager().Queue()  # 创建进程队列
    for i in range(50):
        q3.put("http://www.baidu.com")

    pop = Pool(3)  # 创建3个进程池
    for i in range(q.qsize()):
        pop.apply(les, args=(q,))  # 同步执行，同步比异步快在任务相对少时
        # pop.apply_async(les, args=(q,))         # 异步执行
    pop.close()  # 关闭进程池
    pop.join()  # 主线程等子线程运行结束在执行主线程
    es = time.time()
    print("执行时长{}".format(es - ts))


def wes():
    for i in range(10):
        print("第一个任务执行{}次".format(i))
        requests.post("http://www.baidu.com")


def wsd():
    for i in range(10):
        print("第二个任务执行{}次".format(i))
        requests.post("http://www.baidu.com")


# monkey.patch_all()
g1 = greenlet.greenlet(wes)
g2 = greenlet.greenlet(wsd)

g3 = gevent.spawn(wes)   # 创建两个协程并执行，协程存在线程之中，线程默认不等待协程执行
g4 = gevent.spawn(wsd)   # 第一个参数执行任务，
# g3.join()               # 让线程等待协程，时间参数不传默认等待协程执行完毕
# g4.join()                # 两个任务不是同步执行，先执行完任务1在执行任务2，默认不切换


def time_count(func):                           # 计算时间的装饰器
    def wrapper(*args, **kwargs):
        print("开始执行")
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("执行结束，总耗时{}s".format(end_time - start_time))
    return wrapper


def green_work(q, gname):                           # 创建协程任务
    count = 0
    while not q.empty():
        try:
            url = q.get(timeout=0.01)
            requests.get(url)
            gevent.sleep(0.001)
            count += 1
        except Exception as e:
            raise e
    print("---协程{}执行了{}次任务----".format(gname, count))


def thread_work(q, tname):                          # 创建3个线程，运行协程
    g_list = []
    for i in range(5):
        gname = "{}_线程_{}".format(tname, i)
        print("线程名称{}".format(gname))
        g = gevent.spawn(green_work, q, gname)
        g_list.append(g)
    gevent.joinall(g_list)                          # 可以接收一个列表，主线程等待子线程


def process_work(q, pname):                         # 创建2进程任务，运行线程
    t_list = []
    for i in range(3):
        tname = "{}_进程_{}".format(pname, i)
        print("创建线程{}".format(tname))
        t = threading.Thread(target=thread_work, args=(q, tname))
        t_list.append(t)
        t.start()
    for t in t_list:                                # 让主线程等待子线程
        t.join()


@time_count
def main():                                         # 创建队列函数
    q = Queue()
    for i in range(1, 10001):                       # 创建10000任务放入队列
        q.put('http://127.0.0.1:5000/')             # 向队列写数据
    print("队列创建完成队列数{}".format(q.qsize()))
    pro_list = []                                       # 创建列表存放进程
    for j in range(2):                                  # 循环创建两个线程放到列表，然后启动
        pname = "进程_{}".format(j)
        print("线程名称{}".format(pname))
        p = Process(target=process_work, args=(q, pname))
        p.start()
        pro_list.append(p)
    for p in pro_list:                                  # 让主进程等待子进程
        p.join()


if __name__ == '__main__':
    main()



