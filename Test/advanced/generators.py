def firstn(n):
    num = 0
    while(num < n):
        yield num
        num += 1

for i in firstn(20000):
    print(i)

# it yields the latest item, and also it has the memory to know where the last stat was