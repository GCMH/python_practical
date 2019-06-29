# 定义一个函数，函数名字为show，无参
def show():
    print("show")


def sum(n):
    i, s = 0, 0
    while i <= n:
        s += i  # s = s + i
        i += 1
        
    return s


def pow(x, y=2):
    return x ** y

def add(*nums):  # 可变参数
    print(type(nums))
    s = 0
    for i in nums:
        s += i
    return s

def show_stu(**kw):  # 关键字参数
    for k, v in kw.items():
        print(k, v)

def show_book(*, bid, name, price=50,author = "gcmh"):
    print(bid, name, price)

show_book(name="Python程序设计", bid=1001, price=33, author="gcmh")

show_stu(sno=1001, name="张三", sex="男")

s = {"sno": 1002, "name": "李四", "sex": "女", 'phone': '18532432234'}
show_stu(**s)


print(add(*[1, 2, 3, 4]))
print(add(1, 2))
print(add(1, 2, 3))
print(add())

print(pow(3))
print(pow(3, 3))




show()  # 调用show函数
print(show())
print(sum(100))


i = 3
j = 5

# tmp = i
# i = j
# j = tmp

# i = i + j
# j = i - j
# i = i - j

i, j = j, i

# a = j
# b = i
# i = a
# j = b

print(i, j)

