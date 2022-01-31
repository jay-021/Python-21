from cgi import print_directory


x = [[1,2,3], ["a","b","c"]]
for i in x:
    #here the all list is consider as a i 
    for j in i :
        #here the two sub list of i is consider as a j
        print(j,end="")
    print()

