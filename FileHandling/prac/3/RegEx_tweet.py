import re
text = "Nigger Cock or White Rape #niggercock #whiterape"
pattern = r'#[a-zA-Z0-9]{1,}'

x = re.findall(pattern,text)
print(x)