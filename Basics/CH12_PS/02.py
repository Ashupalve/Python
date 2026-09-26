# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.


l = [12,1,25,36,47,58,65,32,15,35,11,8]
print(type(l))

for i ,item in enumerate(l):
    if i == 2 or i == 4 or i == 6 :
        print(item)