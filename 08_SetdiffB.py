# PY2
# https://www.hackerrank.com/challenges/py-check-subset/problem

T = int(raw_input())
for i in range(T):
    n = int(raw_input())
    setA = set(map(int, raw_input().split()))

    m = int(raw_input())
    setB = set(map(int, raw_input().split()))

    print len(setA.difference(setB)) == 0
