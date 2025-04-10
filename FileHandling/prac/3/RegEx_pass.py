import re
text = ["Dhruvsingh@123","dhruvsingh123","Whatwouldmeekdo@6"]
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%&*!?])[a-zA-Z0-9!@#$%&*?]{8,}'

for i in text:
    if re.match(pattern,i):
        print(f"The password {i} is strong")
    else:
        print(f"The password {i} is not strong")