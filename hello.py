#write a program to accept percentage from the user and display the
# grade accoding to  the following criteria
#marks 
# >90
# >80 and <=90
# >=60 and <=80
# below 60
# 90


# 
# 
# grade 
# A
# B
# C
# # D
# per = int(input("percentage"))
# if per > 90:
#     print("Grade is A")
# if per > 80 and per <=90:
#     print("Grade is B")
# if per >=60 and per <= 80:
#     print("Grade is C")
# if per < 60:
#     print("Grade is D")


# Take input of length and breadth of a rectangle from user and print area of it.

def  area():
    
   length=int(input("enter the length"))
   breadth=int(input("enter the width"))
   result=length*breadth
print(result)
area()

days=("mon","tue","wed","thur","fri","sat","sun")
print(type(days))