#print the biggest number


a=float(input("ENTER THE 1ST NUMBER: "))
b=float(input("ENTER THE 2ND NUMBER: "))
c=float(input("ENTER THE 3RD NUMBER: "))
d=float(input("ENTER THE 4TH  NUMBER: "))
e=float(input("ENTER THE 5TH NUMBER:  "))
max=a
if(b>max):
    max=b
if(c>max):
    max=c
if(d>max):
    max=d
if(e>max):
    max=e
print("the biggerst number",max)


#print the greater number

n1=int(input("enter the 1st number:  "))
n2=int(input("enter the 2nd number:  "))
if(n1>n2):
    print(n1,"is greater")
else:
    print(n2," is greater")



#total marks average percentage


b=float(input("BENGALI"))
e=float(input("ENGLISH"))
m=float(input("MATH"))
s=float(input("SCIENCE"))
g=float(input("GEOGRAPHY"))
total=(b+e+m+s+g)
avg=(total/5)
per=((total/500)*100)
print("average: ",avg)
print("percentage: ",per)