# purchase                discount
#below 5000                 5%
#5000-7500                  10%
#7501-10000                 15%
#10000<p                    20%

purchase=int(input("ENTER PURCHASE AMOUNT:  "))
if(purchase<5000):
    purchase=purchase-(purchase*0.05)
if(5000<purchase<7000):
    purchase=purchase-(purchase*0.1)
if(7501<purchase<10000):
    purchase=purchase-(purchase*0.15)
if(1000<purchase):
    purchase=purchase-(purchase*0.2)
print("purchase amount is",purchase)
