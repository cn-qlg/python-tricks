"""知识点：
bool变量可作为int类型变量使用
True -> 1
False -> 0"""

# 通常用法
age = 20

if age >= 18:
    print("我已经是一个成年人了")
else:
    print("我还未成年")

# or
print("我已经是一个成年人了" if age >= 18 else "我还未成年")

# 小技巧
print(["我还未成年", "我已经是一个成年人了", ][age >= 18])
