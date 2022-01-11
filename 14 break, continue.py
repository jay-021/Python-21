students = ["radha","kanha","ram","sita","rukmani","mira"]
# now we create a loop which prints every name 
    
for student in students :
        if student == "sita":
            break;
        print(student)

print("************************************************")

# now we use continue to skip any value or name in our loop

for student in students :
    if student == "sita":
        continue;
        
print(student)