x = 2 ** 8 # Exponential
print(x)

# # Working with inputs
# a = int(input('Int number A: '))
# b = float(input('Float number B: '))
# print(a)
# print(b)

# # Convert to string
# var = 91
# print( str(var % 10) + str(var // 10) )



# # Booleans
# x = 5 == 5
# print(x)
# print(type(x))

# x = 5>4 or 7>=2 and 4>=6 
# print(x)



# # if / else
# x = int(input("enter a number: "))

# if x % 2 == 0:
#     output = 'to 2'
# elif x % 3 == 0:
#     output = 'to 3'
# else:
#     output = 'not to 2 and 3'    
# print('x is ' + output)



# # How to run python on terminal? $ python3
# # How to run a pyhton file on terminal?
# #   1. goto dir
# #   2. $ python3 yourfile.py (or $ python3 "the whole path")



# # Functions
# def square(input):
#     return input * input

# print(square(4))



# While and For

x = 10
while x > 0:
    print(x)
    x -= 1

for i in range(1,10):
    print(i)
    if i == 5:
        break

customRange = [1,3,5,7,8]
for item in customRange:
    print(item**2)

stringRange = ['Khaled', 'Meri']
for item in stringRange:
    print('Hey', item)

print("*****")

str = 'Mehrdad'
for i in range(0,len(str)):
    print(i, str[i])

for letter in str:
    print(letter)

# Slice the string
print("the first 3 characters:", str[:3])
print("the 4th characters till end:", str[3:])
print("the last 3 characters:", str[-3:])
print("the last character:", str[-1])

# Check the substring
print ('ehr' in str)


# Extract all the extension methods of a data type
print(dir('jadi'))

print('Put your mind at ease'.count('a'))
print('            Put   your    mind at ease'.strip())

#string formatting
print('Hello %s You are %s yeas old' %('Mehrdad', '31') )

# lists
l1 = [1, 5.46, 'Jadi']
l2 = [l1, [3, 65]];

for i in l2:
    print(i)

l1 = [1,2]
l2 = ['a', 'b']

print(l1 + l2)
print(dir(l1))
l1.append('new')
print(l1)
del l1[2]
l1.append(6)
l1.sort()
print(l1)


# pup
l1.pop()
print(l1)

str = "This is a sample text"
print(str.split())

print('-'.join(str.split()))

#dictionaries
dic = dict()
f2t = dict()
f2t['yek'] = 'bir'
f2t['do'] = 'ikki'

print(f2t['do'])
print(f2t)

dic = {'one': 1, 'two': 2}
print(dic.keys())
print(dic.values())
print('three' in dic)

# word counter
wordCounter = dict()
str = 'This is a simple text, just for fun'
str = str.lower()
str = str.replace(' ', '')
for letter in str:
    if letter in wordCounter:
        wordCounter[letter] += 1
    else:
        wordCounter[letter] = 1

mylist = list(wordCounter.keys())
print(mylist)
mylist.sort()
for letter in mylist:
    print('%s: %s' %(letter, wordCounter.get(letter)))

# tuple: the difference with lists, tuples are immutable!
mytuple = tuple
mytuple = (1,2,3)

def returnTuple(): # it can return tuple
    return 1,3

a, b = returnTuple()
print(a,b)

print(type(mytuple))

# Converting a dictionary to tuples
mydic = {"ali": 19, "mahsa": 22, "arman": 18}
print(list(mydic.items()))
for name, age in list(mydic.items()):
    print('%s age is %s' %(name, age))