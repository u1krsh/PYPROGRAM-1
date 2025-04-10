import re

text = "user1@gmail.com message.utkarshsingh@gmail.co.in"
pattern = r'@([A-Za-z.]{2,})'
x = re.findall(pattern,text)
print(x)
