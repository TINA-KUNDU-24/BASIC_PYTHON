# reverse and integer number

n=int(input("ENTER THE NUMBER: "))
sum=0
while(n!=0):
    r=n%10
    sum=sum*10+r
    n=n//10
print("the reverse no is: ",sum)

# print 'n' number of integer number sequently

n=int(input("ENTER THE RANGE: "))
i=1
while(i<=n):
    print(i)
    i+=1