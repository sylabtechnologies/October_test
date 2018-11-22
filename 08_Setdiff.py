# PY2
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

if __name__ == '__main__':
    e = int(raw_input())
    engl = set(map(int, raw_input().split()))
    f = int(raw_input())
    frnc = set(map(int, raw_input().split()))

    print len(engl.difference(frnc))

