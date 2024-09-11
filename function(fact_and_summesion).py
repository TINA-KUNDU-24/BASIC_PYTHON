# factorial of a number using function.

def fact():
    n=int(input("ENTER THE NUMBER: "))
    fact=1
    for item in range (1,n+1):
        fact=fact*item
        
    print("the factorial is: ",fact)
fact()

# summation of number using function.

def sum ():
    a=int(input("ENTER THE 1ST NO:  "))
    b=int(input("enter the 2nd number:  "))
    print("the sum is",a+b)
sum()