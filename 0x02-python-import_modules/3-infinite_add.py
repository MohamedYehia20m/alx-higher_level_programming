#!/usr/bin/python3
import sys


def printsum():
    x = len(sys.argv)
    sum = 0
    for i in range(1, x):
        sum += int(sys.argv[i])
    print('{:d}'.format(sum))


if __name__ == "__main__":
    printsum()
