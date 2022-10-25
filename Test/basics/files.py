import os

f = open(os.getcwd() + '/Test/scores.txt')

# To insert multiple lines in python
# a = '''12
# '''

sum = counter = 0

for line in f:
    counter +=1
    sum = float(line.strip()) # use strip (or rstrip) to remove enters, tabs, and spaces

print('Sum is %s' %sum)
print('Total count is %s' %counter)
print('Average is %a' %(sum/counter))

outf = open(os.getcwd() + '/Test/scores-output.txt', 'w')
outf.write('Average of scores: %a' %str(sum/counter))

f.close()
outf.close()