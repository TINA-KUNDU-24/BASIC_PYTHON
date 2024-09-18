# WRITE A PYTHON PROGRAM TO DETERMINE THE 'N'TH ELEMENT OF THE ARITHMETIC SEQUENCE WHERE THE 1ST TERM A=7 
# AND THE COMMON DIFFERENCE D=11 . TAKE THE USER GIVEN INPUT FOR VALUE OF 'N' AND THEN COMPUTE AND PRINT 
# THE 'N' ELEMENT OF THE SEQUENCE ..

a=7
d=11
n=int(input("ENTER THE NUMBER: "))
for i in range(1,n):
    a=a+d
print(a)

#TAKE A LIST WITH SOME INTEGER VALUES AND PRINT THE 2ND HIGHEST NUMBER OF THIS LIST ..
list=[]
for i in range(5):
    list.append(int(input("ENTER NUMBER: ")))
list1=sorted(list)
print("THE LIST 1 IS: ",(list1))
print ("THE MAXIMUM NUBER IN LIST 1: ",(max(list1)))
list1.remove(max(list1))
second_highest=max(list1)
print("THE SECOND HIGHEST NUMBER IS: ",second_highest)

#TAKE A LIST WITH SAME NUMBER AND WRITE A PROGRAM TO CREATE A NEW LIST WHICH CONTENTS THE NUMBER ,WHICH
# ARE EITHER DIVISIBLE BY 5 OR 7 AND BOTH AND PRINT A NEW LIST IN A ASCENDING ORDER..
l=[]
l1=[]
for i in range(5):
    l.append(int(input("ENTER NUMBER: ")))
print("THE LIST IS: ",l)
for i in l:
    if(i%5==0 or i%7==0):
        l1.append(i)
    else:
        l.remove(i)
print("THE LIST 1 IS: ",l1)