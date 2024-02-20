def solution(answers):
    point = []
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    ab = 0
    bb = 0
    cb = 0
    
    for i, j in enumerate(answers):
        if j == a[i%len(a)]:
            ab += 1
        if j == b[i%len(b)]:
            bb += 1
        if j == c[i%len(c)]:
            cb += 1
        
    maxpoint = max(ab,bb,cb)
    
    if ab == maxpoint:
        point.append(1)
    if bb == maxpoint:
        point.append(2)
    if cb == maxpoint:
        point.append(3)
        
    point.sort()
    
    
    return point
    
        
        