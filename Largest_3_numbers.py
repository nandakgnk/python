##Author: Nanda Kishore
#Desc: To find largest of 3 numbers. 

num1=input()
num2=input()
num3=input()

if  num1 == num2 and num3 == num1:
    print("All numers are equal and the given numbers is:", num1 )
elif num1 == num2:
    print("The 1 and 2 numbers are equal")
elif num1 == num3:
    print("The 1 and 3 numbers are equal" )
elif num2 == num3:
    print("The 2 and 3 numbers are equal")
else:
    if num1 >= num2 and num1 >=num3:
        print("\n""The Largest number in the list is 1st Element", num1)
    elif num2 >= num3 and num2 >= num1:
        print("\n""The Largest number in the list is Middle Element",num2)
    else:
        print("\n""The Largest number in the list is last Element",num3)
