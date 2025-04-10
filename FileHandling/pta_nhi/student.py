def display():
    with open("student.csv", "r") as f:
        x = f.readline()
        while x != "":
            print(f"Details: " , x)
            x = f.readline()
    f.close()
            
def add_student(name,section,roll):
    with open("student.csv", "a") as f:
        f.write(f"\n{name},{section},{roll}")
    f.close()

display()
name = str(input("Student Name:"))
section = str(input("Section:"))
roll = int(input("Roll: "))
add_student(name,section,roll)
display()

    