# 1157 단어공부
# 주어진 문자열에서 가장 많이 사용된 알파벳 출력

# 입력된 문자를 모두 대문자로 치환해서 받아드림
input =  list(str(input()).upper())

dict = dict()

for i in list(set(input)):
    dict[i] = 0

# 특정 알파벳 사용 횟수를 dictionary에 저장
for i in input:
    dict[i] += 1
    
# 제일 많이 사용한 알파벳은 몇번 사용되었는지 확인 
max_value = max(dict.values())

# 가장 많이 사용된 알파벳의 갯수를 확인
count = 0
for i in dict.keys():
    if(dict[i] == max_value):
        count += 1
        
# 여러개인 경우 ? 출력
if(count > 1):
    print("?")
    
# 하나인 경우 알파벳 출력
else:
    for key, value in dict.items():
        if (value == max_value):
            print(key)
