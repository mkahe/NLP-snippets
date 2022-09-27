from nltk import edit_distance
from scipy.spatial.distance import cosine

rating_matrix  = [[3,7,4,9,9,7],
                  [7,0,5,3,8,8],
                  [7,5,5,0,8,4],
                  [5,6,8,5,9,8],
                  [5,8,8,8,10,9],
                  [7,7,0,4,7,8]]

Items = ['The school art','Schooling Kids','Closing Schools',
'Military School','This is a military school','School Book']

Similarities = []
Edit_Distyances = []
     
for i in range(0,len(rating_matrix)):
    if i != 2:
        Similarities.append((i,cosine(rating_matrix[2],rating_matrix[i])))
        
Min = min(Similarities, key = lambda t: t[1])
print('In here the colosest user to the user 3 is',Min[0]+1,'with distance =',round(Min[1],4))
print('The recommended Value of item 4 for the user 3 is',rating_matrix[Min[0]][3])
print('if the ranking value is beyond 5, it means that this item will be recommaned user 3')
print('__________________________________________________')
for i in range(0,len(Items)):
    if i != 3:
       Edit_Distyances.append((i,edit_distance(Items[3],Items[i])))

Min = min(Edit_Distyances, key = lambda t: t[1])
print('In here the colosest item to the item 4 is',Min[0]+1,'with edit distance =',round(Min[1],4))
print('The recommended Value of item 4 for the user 3 =',rating_matrix[3][Min[0]])
print('if the ranking value is beyond 5, it means that this item will be recommaned user 3')

print('This is one of the interpretation of solving the problem')
