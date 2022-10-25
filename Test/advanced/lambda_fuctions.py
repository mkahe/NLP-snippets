myfunc = lambda x: x**2
print(myfunc(4))

# example of using lambda: sorting a list by the second element
a = [(3, 5), (7,1), (2,2)]
a.sort(key = lambda x: x[1])
print(a)

mapList = [2, 6, 4]
mapOutput = map(lambda x: x*2, mapList)
print(mapOutput)
print(list(mapOutput))

numbers = [2, 10, 14, 7]

output = list(map(lambda x: 'big' if x >= 10 else 'small', numbers))

print(output)

filterList = [2,3,4,5,6,7,8,9,10]
output = list(filter(lambda x: x%2 ==0, filterList))
print (output)