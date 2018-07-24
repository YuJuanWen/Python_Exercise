def calNum(num):
    if num>=1:
        result=num*calNum(num-1)

    else:
        result=1
    return result

ret=calNum(6)
print(ret)