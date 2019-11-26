
# 使用切片方法
a = [1, 2, 3, 4, 5]
b = a[:]
print(a, b, id(a), id(b))


# 通过添加一个空列表
a = [1, 2, 3, 4, 5]
b = a + []
print(a, b, id(a), id(b))

# 通过类型转换
a = [1, 2, 3, 4, 5]
b = list(a)
print(a, b, id(a), id(b))

# 调用list.copy方法
a = [1, 2, 3, 4, 5]
b = a.copy()
print(a, b, id(a), id(b))
