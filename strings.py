#d = "ABCDEFG"
#d[0:3]
#e = 'clocrkr1e1c1t'
#e[::2]
#print("Hola esto es un \\ backslash!")
#f = "You are wrong"
#f.upper()
import re
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
pattern = r"Mary"
replacement = "Bob"
new_string = re.sub(pattern, replacement, g, flags=re.IGNORECASE)
print(new_string)