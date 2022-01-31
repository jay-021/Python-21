#Loop control stetment - 
# break is the first loop control stetamemt who stop the loop at perticular point
x = "Hey there, this is jay mathukiya"
for i in x :
    if i == "s" :
        break
    print(i,end="")


#continue : skip the statement following it and returns control to the beginning of the loop
for i in [1,2,3,10,11,00,12,13,33]:
    if i > 10 :
        continue
    print(i)