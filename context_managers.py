"""使用Python内置的上下文管理器"""

# 通常用法
f = open("example.txt", "w")
f.write("hello, world")
f.close()

# 如果以上代码在尝试执行f.write("hello, world")的时候，出现错误，则可能导致文件没有正确关闭
# 所以，需要加上一些异常处理。
# 由于finally是一定会执行到的，所以可以确保文件被关闭
f = open("example.txt", "w")
try:
    f.write("hello, world")
finally:
    f.close()

# 小技巧
with open("example.txt", "w") as f:
    f.write("hello, world")

# 原理
# 上下文管理器(context manager)
# What? 什么是上下文管理器(context manager)?
#   It’s a simple "protocol" (or interface) that your object needs to follow in order to support the with statement.(摘自Python Tricks A Buffet of Awesome Python Features)
#   上下文管理器(context manager)就是一个协议或者一个接口，当你的对象实现了这个协议（接口），就可以支持with语句。
# Why? 为什么要使用上下文管理器(context manager), 有什么用处？
#   它通过抽象一些常见的资源管理模式的功能，并允许对它们进行分解和重用，从而帮助简化这些模式。简单来说实现了这个协议（接口），就可以在使用的时候得到简化。
#   就像上面一样，不用每次都写一个try-finally，而且不用担心，因为漏了，而导致文件或者其他对象没有正确关闭。
#   在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍的。 
#   这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正确运行。
# How? 怎么用?
#   需要对象需要实现__enter__和__exit__方法。Python会在合适的时间里，调用者两个方法。
# 所以上面的open()语句，就可以像这样使用。

# Python会在调用with语句自动执行__enter__方法来获取资源。然后当离开了这段代码块之后，会自动调用__exit__方法来释放资源。
class ManagedFile:

    def __init__(self, name):

        self.name = name

    def __enter__(self):

        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self.file:
            self.file.close()

with ManagedFile("example.txt") as f:
    f.write("hello world again.")


# 小技巧
# python现在内部实现了一个contextlib.contextmanager装饰器，来帮你更简单地使用。
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


with managed_file("example.txt") as f:
    f.write("hello world again.")
