stud_num = int(input("Enter Number of students: "))
lst = []
for i in range(1,stud_num+1):
    grad = int(input(f"Enter grade for student {i}: "))
    lst.append(grad)

avg = sum(lst)/len(lst)
print(f"The average of {stud_num} students is {avg}")

