####Super Market Application:
###Author: Nanda Kishore
###Desc: Super market application to caliculate Banana Dozens prices
##### If customer took 2 Dozens of Banana its costs 5/- for 2 Doznes, else if picked 1 dzone cost is 3/- for Dozen

dzns=2
cname=input("Enter Customer name:")
print("Thanks for Buying Banana's", cname)

class store:
    def __init__(self, fruits,qty):
        self.fruits = fruits
        self.qty = qty
        
print("Thanks for Buying Banana's")
items=store("Banana",input())
value1=int(items.qty)
print("Shop offer: Cost of 2 dozans is 5 and cost of 1 dozan is 3")
if value1 == 1:
    value2=int(value1*3)
    print("The Price of the fruits is", value2)
else:
    cst1=int(value1/dzns)
    cst2=int(value1%dzns)
    L_qty1=cst1*5
    L_qty2=cst2*3
    L_qty4=L_qty1+L_qty2
    print("The total bill", "on Banana","is", int(L_qty4))
