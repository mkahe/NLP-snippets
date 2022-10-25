import csv
import os
import hashlib

rainbow_dic = dict()
for i in range(1, 9999): 
    hash = hashlib.sha256(str(i).encode('utf-8')).hexdigest()
    rainbow_dic[hash] = i

with open(os.getcwd() + '/Test/rainbow_table/rainbow_table.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] in rainbow_dic:
            print("Yoo! I hacked the password of %s. the password is: %s and the hash is %s" %(row[0], rainbow_dic[row[1]], row[1]))