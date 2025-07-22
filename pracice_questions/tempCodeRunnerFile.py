name = input("enter a string to reverse: ")
for i in range(0,(name.__len__() ) // 2):
    temp=i
    i=name[(name.__len__())-1]
    name[(name.__len__() )-1] = i

print(name)
