sumi=lambda arg1, arg2: arg1+arg2

print("value of total:", sumi(10,30))

stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]

stus.sort(key=lambda x:x['age'])
print(stus)