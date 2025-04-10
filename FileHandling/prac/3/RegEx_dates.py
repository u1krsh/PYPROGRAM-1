import re
text = "John's birthday is on 12-05-1998, and Lisa's is on 23/09/2001. Another date is 01-01-2020."
patter = '[0-9]{2}[-/][0-9]{2}[-/][0-9]{4}'
x = re.findall(patter,text)
print(x)