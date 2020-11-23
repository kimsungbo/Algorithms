# 1193 분수찾기
# 분수의 순서에서 규칙을 찾는 문제

x = int(input())

line = 1

# 입력된 숫자가 몇번째 사선에 위치한지 확인
while True:
    if x <= sum([i for i in range(1, line + 1)]):
        break
    else:
        line += 1
        
        
pos = line - (sum([i for i in range(1, line + 1)]) - x)

# 짝수 라인일 경우 
if line % 2 == 0:
    print(pos, '/' , (line + 1 -pos), sep="")

# 홀수 라인일 경우 (짝수라인일 경우와 분모분자 반대)
else:
    print((line + 1 -pos), '/' , pos, sep="")