# ZOKORIA https://www.hackerrank.com/contests/hourrank-31/challenges/save-the-queen
# PY2

def coundId(s):
    idx = len(s) - 1
    rpoint = s[idx]
    ans = 0
    
    while idx >= 0:
        if s[idx] != rpoint:
            break
        ans += 1
        idx -= 1
        
    return ans

def distribute(fite, points):

    howmany = coundId(fite)
    
    if howmany > 1 :
        delta = fite[-howmany-1] - fite[-1]
        available = float(points)/howmany
        if available > delta:
            points = delta*howmany
        else :
            delta = available
            points = 0

        idx = len(fite) - 1
        while howmany > 0:
            fite[idx] += delta
            howmany -= 1
            idx -= 1

    else:
        if len(fite) == 1:
            delta = points
            points = 0
        else :
            delta = fite[-2] - fite[-1]
            if delta > points :
                delta = points
                points = 0
            else :
                points -= delta

        fite[-1] += delta

    return points

def solve(n, s):
    
    s.sort()
    s.reverse()
    fite = s[:n]
    reserve = s[n:]
    
    for x in reserve:
        while x > 0 :
            x = distribute(fite, x)
        
    print min(fite)
        

if __name__ == '__main__':
    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = map(int, raw_input().rstrip().split())

    solve(n, a)
