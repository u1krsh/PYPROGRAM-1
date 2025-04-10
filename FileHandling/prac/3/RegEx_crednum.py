import re

pattern = r'[0-9]{4}-[0-9]{4}-[0-9]{4}-([0-9]{4})'

text = "1234-5678-1234-5678"
rep = r'XXXX-XXXX-XXXX-\1'
x = re.sub(pattern,rep,text)
print(x)