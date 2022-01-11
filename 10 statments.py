age = input ("Enter your age") 

#statements are use for exicute maltiple conditions
# first statement is "if"

if int(age) >= 18:
    print ("You are an adult.")

# when we want to add multiple condititions there we use "elif"

elif int(age) < 18 and int(age) > 5:
    print ("You are a kid who is going to school.")
    
# when our all conditition became fell then "else" statement exicute

else :
    print ("ohh ! You are cute little baby ")

print ("Thank you ")