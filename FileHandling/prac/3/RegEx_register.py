#KA-05-MD-1234
import re

text = "KA-05-MD-1234"
pattern = r'[a-zA-Z]{2}-[0-9]{2}-[a-zA-Z]{2}-[0-9]{4}'

if re.match(pattern,text):
    print("Yes")