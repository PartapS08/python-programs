var={'a':0,'b':23,'c':40,1:'java',2:'python',3:'ruby'}

list=[]
for i in var.keys():
    if type(i)==str:
        list.append(i)

print(list)