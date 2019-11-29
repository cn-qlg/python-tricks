"""下划线的几种用法。
1. 单下划线 _
2. 一个前缀下划线 _val
3. 一个后缀下划线 val_
4. 两个前缀下划线 __val
5. 前后各两个下划线 __val__"""

"""1. 单下划线 _"""
# 通常用来作为临时变量，或者在解包的时候用于忽略变量使用
for _ in range(10):
    print(_)

name, age, _, tel = ("Jack", 18, "上海市静安区XX路XX号", "18712345678")
print(name, age, tel)

# 特殊用法，在python执行环境里，代表上一个表达式的结果
# >>>my_list = [1, 2, 3, 4, 6, 7]
# >>>len(my_list)
# 6
# >>>_
# 6
# >>>

"""2. 一个前缀下划线 _val"""
# 仅仅是一个约定习惯，用来提醒其他程序员，这是一个内部变量或内部方法。


class Test2:
    def __init__(self):
        self.x = 1
        self._y = 2

    def say_hello(self):
        print("hello")

    def _say_world(self):
        print("world")


t2 = Test2()
print(t2.x, t2._y)
t2.say_hello()
t2._say_world()

# 但是需要注意的是，如果从其他模块导入的话，会有区别。
# 除非在__all__中定义了，否则python不会导入以下划线开头的元素
# my_module.py:
# def external_func():
#     return 23

# def _internal_func():
#     return 42

# >>>from my_module import *
# >>>external_func()
# 23
# >>>_internal_func()
# NameError: "name '_internal_func' is not defined"

# 但是如果使用另一种方式导入，则不会出现在这种问题
# >>>import my_module import
# >>>my_module.external_func()
# 23
# >>>my_module._internal_func()
# 42
# 所以尽量不要使用from module import *这种方式

"""3. 一个后缀下划线 val_"""
# 此种方式仅仅用于避免与系统关键字重复
# def make_object(name, class):
#     pass
# 将会报出如下错误
# SyntaxError: invalid syntax
# 但是改成下面这样，就没事里
# def make_object(name, class_):
#     pass

"""4. 两个前缀下划线 __val"""
# 常用做表示私有变量private


class Test4:
    def __init__(self):
        self.public_val = "public value"
        self.__private_val = "private value"

    def get_private_val(self):
        return self.__private_val

t4 = Test4()
print(t4.public_val)
print(t4.get_private_val())
# print(t4.__private_val)  # AttributeError: 'Test4' object has no attribute '__private_val'
# 但是实际上，__private_val是存在的，只不过被“改名”
print(t4._Test4__private_val)
# Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问
# 之所以这样设定，可以用这样一句名言加以解释，就是"We are all consenting adults here"。
# 因为绝大多数程序员都认为开放比封闭要好，而且程序员要自己为自己的行为负责。

# 另外需要注意一点的是，在命名变量的时候，应该尽量避免出现_Test4__private_val这种形式
_Test4Confilct__private_val = "GlobalValue"


class Test4Confilct:
    def __init__(self):
        pass
    def get_public_value(self):
        return public_value
    def get_private_val(self):
        return __private_val
t4c = Test4Confilct()
print(t4c.get_private_val())
# print(t4c.get_public_value()) # NameError: name 'public_value' is not defined
# 同样两个变量，都没有声明，但是public_value不能使用，但是__private_value可以
# 就是因为"改名"，使得出现了这种问题。

"""5. 前后各两个下划线 __val__"""
# 这种情况，在python中具有特殊用处，例如__init__，以及__str__等等。前者用于创建对象，后者用于格式化输出对象。
# 当然我们也可以定义这种形式的变量或者方法，并且可以正常使用，Python解释器并不会做出例如"改名"这种操作。


class Test5:
    def __init__(self):
        self.__bam__ = 42
    def __say_hello__(self):
        print("hello")


t5 = Test5()
print(t5.__bam__)
t5.__say_hello__()
