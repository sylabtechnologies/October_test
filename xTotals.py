# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

n = int(input())

dict = {}
items = []
for i in range(n) :
    line = input().split()
    price = int(line[-1])
    
    item = ' '.join(line[0:-1])
    
    if item in dict :
        dict[item] += price
    else :
        dict[item] = price
        items.append(item)

for elem in items :
    print(elem, dict[elem])
    