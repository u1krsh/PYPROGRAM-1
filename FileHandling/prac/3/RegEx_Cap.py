import re

pattern = r'\b[A-Z][a-z]{0,}\b'
text = "Alice and Bob went to New York for a Python Conference."
x = re.findall(pattern,text)
print(x)