a=int(input("ENTER THE RANGE: "))
for item in range(1,a+1):
    if(item%3==0 and item%5==0):
        print(item,"fizzbuzz")
    elif(item%3==0):
        print(item,"fizz")
    elif(item%5==0):
        print(item,"buzz")
    else:
        print(item,"nothing")
                  