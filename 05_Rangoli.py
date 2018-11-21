# PY2
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

# build a pattern step by step
def rangoli(rang, howmany) :

    rev = reversed(rang)
    
    rev = ''.join(rev)
    rev = rev[:howmany]

    revrev = reversed(rev)
    revrev = ''.join(revrev)

    if len(rev) > 1 :
        revrev = revrev[1:]
        rev += revrev

    rlist = list()
    for x in rev :
        rlist.append(x)

    return '-'.join(rlist)

def print_rangoli(size):
    abc = string.ascii_lowercase
    rang = list()
    for x in range(size) :
        rang.append(abc[x])

    totalsize = 2*size - 1
    totalsize = totalsize*2 - 1

    for i in range(1, len(rang)+1) :
        ans = rangoli(rang, i)
        print ans.center( totalsize, '-')
    
    i = len(rang) - 1
    while i > 0 :
        ans = rangoli(rang, i)
        print ans.center( totalsize, '-')
        i -= 1

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
