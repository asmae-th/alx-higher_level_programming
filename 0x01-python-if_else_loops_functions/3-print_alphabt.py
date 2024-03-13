#!/usr/bin/python3
i = 97
output = ""
while i <= 122:
    if i != 101 and i != 113:
        output += chr(i)
    i += 1

print(output)