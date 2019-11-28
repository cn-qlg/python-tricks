"""统计列表中个元素出现次数，摘自python-cookbook
"""
# 通常用法
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
distinct_words = set(words)
words_cnt = dict()
for word in distinct_words:
    words_cnt[word] = words.count(word)
print(words_cnt)

# 或者
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
distinct_words = set(words)
words_cnt = dict()
for word in words:
    if word in words_cnt:
        words_cnt[word] += 1
    else:
        words_cnt[word] = 1
print(words_cnt)


# 小技巧
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)

# 原理
# 在底层实现上Counter就是一个字典，将元素映射到它出现的次数上。
# 所以也支持字典的一些用法，例如更新
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)

# 甚至“合集”，“差集”等等
a = Counter(words)
b = Counter(morewords)
# “合集”
c = a+b
# “差集”
d = a-b
print(a)
print(b)
print(c)
print(d)
