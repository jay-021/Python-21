###Sum of Even Numbers 
#Given a number N, print sum of all even numbers from 1 to N.
# Python Program to Calculate Sum of Even Numbers from 1 to N
N = int(input())

sum = 0

for i in range(1, N + 1):

    # Check for even or not.
    if((i % 2) == 0):
        sum = sum + i
print(sum)