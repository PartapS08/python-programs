

list1=['Hi', 'bike', 'Hlo', 'sky', 'bus']
list2=['Hello', 'bus', 'Train', 'Bike', 'sky']
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)

print(list3)
