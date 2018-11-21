# PY2
# https://www.hackerrank.com/challenges/ginorts/problem

if __name__ == '__main__':
    myinp  = raw_input()

lcase = list()
ucase = list()

oddig = list()
evdig = list()

for x in myinp :
    if  x >= 'a'and x <= 'z' :
        lcase.append(x)
    elif x >= 'A'and x <= 'Z' :
        ucase.append(x)
    else :
        i = int(x)
        if i % 2 == 1 :
            oddig.append(x)
        else :
            evdig.append(x)

result = sorted(lcase)
result.extend(sorted(ucase))
result.extend(sorted(oddig))
result.extend(sorted(evdig))

print ''.join(result)
