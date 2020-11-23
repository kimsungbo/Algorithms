# 1786 찾기
# KMP 알고리즘

def makeTable(pattern):
    table = [0] * len(pattern)
    
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
            
    return table
    
def KMP(parent, pattern):
    table = makeTable(pattern)
    parentSize = len(parent)
    patternSize = len(pattern)
    
    matched = []

    j = 0
    
    for i in range(parentSize):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]
                
        if parent[i] == pattern[j]:
            if j == patternSize - 1:
                matched.append(i-patternSize + 2)
                j = table[j]
            else:
                j+=1
                
    return matched
        
                
                
parent = str(input())
pattern = str(input())

matched_pattern = KMP(parent, pattern)

print(len(matched_pattern))
for match in matched_pattern:
    print(match)