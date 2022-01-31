#set is a data type which stoers uniqe values in our programe.
#we cannot add similar values in set 
l = [1,2,43,3,4]
s = set(l)
print (s)
print (type(s))
s.add (33)
s.add (33)
print (s)
s.remove (3)
print(s)

#set is a data type where we store uniqe values 

s1 = ([1,2,3,4])
s2 = ([3,4,5,6])
s1.append(s2)
print(s1) 