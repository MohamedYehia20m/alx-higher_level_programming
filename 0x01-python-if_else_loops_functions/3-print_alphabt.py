#!/usr/bin/python3
for i in range(26):
    if i == 4 or i == 16:
        continue
    print(f"{i + 97:c}",end="")
