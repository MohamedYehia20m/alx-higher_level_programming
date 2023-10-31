#!/usr/bin/python3
for i in range(100):
    if (i/10) > (i % 10):
        continue
    if i == 89:
        print(f"{i:d}")
    print(f"{i:02d}", end=", ")
