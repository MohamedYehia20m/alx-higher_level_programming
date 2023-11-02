#!/usr/bin/python3
import sys
def printargv():
    x = len(sys.argv)
    if x == 1:
        print('{:d} arguments.'.format(0))
    elif x == 2:
        print('{:d} argument:'.format(1))
        print('{:d}: {:s}'.format(1, sys.argv[1]))
    else:
        print('{:d} arguments:'.format(x - 1))
        for i in range(1, x):
            print('{:d}: {:s}'.format(i, sys.argv[i]))

if __name__ == "__main__":
    printargv()

