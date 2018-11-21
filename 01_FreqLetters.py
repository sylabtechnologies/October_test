# PY2
# https://www.hackerrank.com/challenges/most-commons/problem

import math
import os
import random
import re
import sys


def extract_max(mydict) :
    mymax = list()
    mymax.append(-1)
    mymax.append('z')
    for x in mydict :
        if mydict[x] > mymax[0] :
            mymax[1] = x
            mymax[0] = mydict[x]

    mydict.pop(mymax[1])
    return mymax

def special_append(mylist, entry) :
    i = 0

    for x in mylist :

        if entry[0] > x[0]:
            break

        if entry[0] == x[0] and entry[1] < x[1]:
            break

        i = i + 1

    mylist.insert(i, entry)


if __name__ == '__main__':
    s = raw_input()

letterDict = dict()

for x in s :
    if x not in letterDict :
        letterDict[x] = 1
    else :
        letterDict[x] += 1

result = list()
result.append(extract_max(letterDict))
special_append(result, extract_max(letterDict))
special_append(result, extract_max(letterDict))

for x in result :
    print x[1], x[0]
