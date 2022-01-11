marks = [92,94,95] 
# we can print whole list using list name
print(marks)

# we can print individual values using their index number
print(marks[0])

# we can print values from reverse directions using - "minise"
print(marks[-1])

# if we want to print some of sequens values then we have to enter index befor and after values
print(marks[0:2])

# if we want to add some value then we use append function
print ("append function")
print("********************************************************")
i = input("enter the number which you want to add :-  ")
i = int(i)
marks.append(i)
print (marks) 

# if we want to add values in perticular places then we have to use "insert" function
print("**************************************************************")
print("add value in perticular place")
j = input ("enter the value which you want to add :-  ")
j = int(j)
k = input ("enter the place where you want to add :-  ")
k = int (k)
k = k-1
marks.insert(k,j)
print(marks)

# if we want to check perticular value in our list then we use "in" function
print ("****************************************************************")
print("Now we are going to check our values in list")
l = input("Which value you want to check  :-  ")
l = int(l)
print (l in marks)

# now we are going to massur length 
print("******************************************************************")
print("to massure length we use length keyword")
print(len(marks))
 #if we want to print wholw list using whilw function then see it
print("******************************************************************")
f = 0
while f < len(marks) :
    print (marks[f])
    f = f + 1

print("*******Now we make our list using this command*************")
# if we want to clear list than we jast use "clear" function
print(" #print-(marks.clear) ")
marks.clear()
print(marks)