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
# D
per = int(input("percentage"))
if per > 90:
    print("Grade is A")
if per > 80 and per <=90:
    print("Grade is B")
if per >=60 and per <= 80:
    print("Grade is C")
if per < 60:
    print("Grade is D")

    