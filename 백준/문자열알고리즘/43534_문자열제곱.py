# 43534 문자열 제곱
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

while True:
    string = input()
    
    if string == '.':
        break
    else:
        table = makeTable(string)
        
        pattern_length = len(string) - table[-1]
        
        if len(string) % pattern_length == 0:
            print(len(string) // pattern_length)
        else:
            print(1)