import re
text = "message.utkarshsingh@gmail.com"
pattern = r'[a-zA-Z0-9.-_]+@[a-zA-Z0-9.]{2,}'
print(re.findall(pattern,text))