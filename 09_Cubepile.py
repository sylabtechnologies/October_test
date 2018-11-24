# PY2
# https://www.hackerrank.com/challenges/piling-up/problemimport collections

import collections
import sys

def solvable(cubeLengths) :
    cubeLengths = collections.deque(cubeLengths)
    last = sys.maxint
    result = True

    while len(cubeLengths) > 0:
        if len(cubeLengths) == 1:
            item = cubeLengths.pop()
        else:
            if cubeLengths[0] < cubeLengths[-1]:
                item = cubeLengths.pop()
            else:
                item = cubeLengths.popleft()

        if item > last:
            return False
        else:
            last = item

    return result

T = int(raw_input())

for i in range(T):
    n = int(raw_input())
    cubes = map(int, raw_input().split())
    if solvable(cubes) :
        print 'Yes'
    else :
        print 'No'


