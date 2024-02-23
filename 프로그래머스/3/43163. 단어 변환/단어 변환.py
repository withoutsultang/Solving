
def solution(begin, target, words):
    answer = 0
    targeter = list(target)
    visited  = []
    if target not in words:
        return 0
    
    def bfs(begin):
        nonlocal answer
        nonlocal targeter
        p = 0
        begine = list(begin) # [h,o,t]
        
        for i in range(len(targeter)):
            if begine[i] == targeter[i]:
                p += 1
            
            if p == (len(begine) - 1):
                answer += 1
                return target
        
        
        for i in words: # "hot"
            if i in visited:
                continue
            q = 0
            comp = list(i) # h,o,t
            for j in range(len(comp)):
                if comp[j] == begine[j]:
                    q += 1
            
            if q == (len(comp) - 1) and begin != target:
                visited.append(i)
                begin = i
                answer += 1
                return begin
        

    for i in range(len(words)):
        if begin == target:
            return answer
        if begin != target:
            begin = bfs(begin)

    
    return answer