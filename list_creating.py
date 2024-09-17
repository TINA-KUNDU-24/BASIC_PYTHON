my_list=['TEA','COFFEE','MILK','SUGAR']
print(my_list)

for item in my_list:
    print(item)
    
my_list.append('biscuit')
print(my_list)

my_list.insert(2,'butter')
print(my_list)

list=[1,2,3,4,5,6,7,8,9,10,10.1]
print("THE MAXIMUM NUMBER IS: ",max(list))
print("THE MINIMUM NUMBER IS: ",min(list))
i=0
for item in list:
    i+=1
print("COUNT: ",i)

vowles=['a','e','i','o','u','A','E','I','O','U']
my_string=input("ENTER THE STRING: ")
for item in my_string:
    if(item in vowles):
        print("*",end="")
    else:
        print(item,end="")
        
#write a program to take a list with some integer values and apply some list function like min,max,sorted,count:
number_list=[1,2,5,9,8,74,5,5,12,5,8,4,3,9,2]
print("\nTHE MAXIMUM NUMBER IS: ",max(number_list))
print("THE MINIMUM NUMBER IS: ",min(number_list))
print("THE SORTED NUMBER LIST IS: ",sorted(number_list))
print("THE LIST COUNT IN 9 NUMBER",number_list.count(9))
print("LENGTH OF THE LIST",len(number_list))


list1=['APPLE','BANANA']
list2=['sugar','tea']
list3=['pinaple','bread']
print(list1+list2+list3)
        









