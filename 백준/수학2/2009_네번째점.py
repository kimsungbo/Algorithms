# 2009 네번째 점
# 직사각형을 완성하는 문제

for i in range(3):
    a, b = map(int, input().split())
    
    if a in dictionary_x.keys():
        dictionary_x[a] += 1
    else:
        dictionary_x[a] = 1
        
    if b in dictionary_y.keys():
        dictionary_y[b] += 1
    else:
        dictionary_y[b] = 1
        
for item in dictionary_x:
    if dictionary_x[item] == 1:
        print(item, end=" ")

for item in dictionary_y:
    if dictionary_y[item] == 1:
        print(item, end=" ")