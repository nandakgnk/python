##Author: Nanda Kishore
#Desc: Print table of the give number
print("Enter Number to multiply:")
num=input()


for mult in range(1,11,1):
    result=int(num)*mult
    print(num, "x", mult, "=",result)
