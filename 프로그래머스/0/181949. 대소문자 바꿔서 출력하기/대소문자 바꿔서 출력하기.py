str = ""

for i in input():
    if i.islower():
        str += i.upper()
    elif i.isupper():
        str += i.lower()
        
print(str)