from collections import deque
def dfs(begin, target, words):
    distance = 0
    visited = [0 for i in words]
    stack = [begin]
    
    while stack:
        node = stack.pop()
        
        if node == target:
            return distance
        
        for i in range(len(words)):
            print(node, words[i])
            print(set(node).difference(words[i]))
            if len([j for j in range(len(words[i])) if words[i][j]!=node[j]]) == 1:
                if visited[i] == 0:
                    visited[i] = 1
                    stack.append(words[i])
            print("stack", stack)
                    
        distance += 1
    
    
    
def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    answer = dfs(begin, target, words)
    print(answer)
    return answer