# PY2

def solve(height, wallPoints, lengths):
    ans = 0
    for i in range(len(wallPoints)) :
        reach = wallPoints[i] - 0.25*lengths[i]
        ladder = int(math.ceil(reach - height))
        if ladder > ans :
            ans = ladder
            
    return ans


