x= int (input ("Enter 1st no. :"))
y= int (input ("Enter 2nd no. :"))
z= int (input ("Enter 3rd no. :"))

l= [x,y,z]

for i in l :
    if i%2 == 0:
        print(f"{i} is even no")
        i+=1
    else:
        print(f"{i} is odd no")
print ("This is even odd code using list")
