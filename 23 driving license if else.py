print ("What is your age ?  :-  ")
age = int(input())

if age<18:
    print("You can not apply for driving license")

elif age>100:
    print ("invalid input")
    
elif age>=18:
    print("You can  apply for driving license")

else :
    print ("plese enter your age")
