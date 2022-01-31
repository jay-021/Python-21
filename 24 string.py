from typing import ItemsView


stg = " welcome to jay's code"

print (stg.upper())
print (stg.lower())

print (stg.find('o'))
print (stg.index('o'))

x=stg.split(" ")
print(x)

print(stg.rpartition(" to "))

stg1= "its"
stg2= "jay's"
stg3= "code"

stg4 = "{} {}, {}!".format(stg1,stg2,stg3)
print(stg4)
