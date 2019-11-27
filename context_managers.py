"""使用Python内置的上下文管理器"""

# 通常用法
f = open("example.txt","w")
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

