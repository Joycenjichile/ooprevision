# use slicing(-1,0,-3)


# str1 = "Javatpoint"
from cgitb import small
import numbers


#1 remove the second last number
def lst():
    list=[2,4,6,8]
    list.pop(2)
    return list
print(lst())

#2 count the number of times monday appears
list=["mon","tue","fri","mon"]
print(list.count("mon"))

#3 print the smallest number
def smallest():
    list=[4,9,1,3,8]
    num=list[0]
    for x in list:
        if x<num:
            num=x
            print(num)
smallest()

#4 print the numbers that are divisible_by_seven
def divisible_by_seven():
    for x in range(100,200):
            if x%7==0:
                print(x)
divisible_by_seven() 

#5 a program that takes two input
num1=int(input("enter number1"))
num2=int(input("enter number2"))
sum=num1+num2
if sum>10:
    print("greater")
elif sum<10:
    print("less")
else:
    sum==10
    print("equal")

#6 list=[1,2,3,4,5] and return true if 4 is present in the list and False if is not in the list
def intergers():
    list=[1,2,3,4,5]
    if 4 in list:
            print(True)
    else:
            print(False)    
intergers()

#7 remove the last fruit in the list and return te list without the removed fruit
def fruits():
    list=["apple","grapes","pineaple"]  
    list.pop(-1)
    return list
print(fruits()) 

# 8 a list of cars and return a sorted list
list=["ford","BMW","volvo"]
list.sort()
print(list)

