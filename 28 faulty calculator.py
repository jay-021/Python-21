
# its definitely  work without any problem
# making a faulty calculator

# taking input from the user and changing into integer
f = input(" enter the First number : ")

# taking 2nd input from user
o = input("enter Operator : ")
# taking 3rd number
s = input("enter the Last number : ")

# making a new variable
new_input = f + o + s

# checking the input
if new_input == "45*3":
    print(555)
elif new_input == "56+9":
    print(77)
elif new_input == "56/6":
    print(4)
elif o == "*":
    print(int(f) * int(s))
elif o == "+":
    print(int(f) + int(s))
elif o == "-":
    print(int(f) - int(s))
elif o == "/":
    print(int(f) / int(s))
