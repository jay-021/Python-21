# we take first operator
first = input("Enter first number :")

# now we take operator which will we use for calculate
operator = input("Enter operator (+,-,*,/,%) :")

# now we take second number
second = input("Enter second number :")

# we have to convert our string variables to integer
first = int(first)
second = int(second)

# now we apply if elif condititions

if operator == "+" :
    print(first + second)

elif operator == "-" :
    print(first - second)

elif operator == "*" :
    print(first * second)

elif operator == "/" :
    print(first / second)

elif operator == "%" :
    print(first % second)

# now we add our last else conditition

else :
    print ("Invalid oprator")

print ("Thank you for using our calculator.")