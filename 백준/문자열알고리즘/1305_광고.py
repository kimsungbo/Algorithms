# 1305 광고
# KMP의 failure function 활용

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

L = int(input())

string = input()

table = makeTable(string)

print(len(string) - table[-1])