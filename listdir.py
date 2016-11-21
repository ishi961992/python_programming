import os
import sys
import re



names=os.listdir("C:\\Users\\ishi961992\\Desktop")
for name in names:
    p=(re.findall(r'\d', name))
    if p!=[]:
        removed=name.replace(p[0],"")
        print (removed)
    else:
        print (name)


