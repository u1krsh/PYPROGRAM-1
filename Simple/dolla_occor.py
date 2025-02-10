#Sat Jan 25 17:16:55 2025

x= str(input("Enter Sentence: "))
count = 0
for i in x:
    if(i=="$"):
        count=count+1
print(count)        
    