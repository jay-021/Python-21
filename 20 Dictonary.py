#Dictonary is nothing but a key value pairs
jp = {"jay" : "mathukiya" , "lalo" : "patel" , "rahul" : "vekariya"}
print(jp)

# to add a new elements in dictonary
jp["parthik"] = "godhani"
print(jp)

#other mathod to add elements in dictonary
jp.update ({"aadesh" : "vaghasiya"})
print(jp)

jp.update({"mj" : {"kb": 8 ,"mj":8 }})
print(jp)

#remove elements from the dictonary
del jp ["mj"]
print(jp)

#Functions in dictonary 
print(jp.keys())
print(jp.keys())

d = {"a":1,"b":2,"c":3}
print(d.values())
keys= ('a','b','c')
value =1
print(dict.fromkeys(keys,value))

d.clear()
print(d)