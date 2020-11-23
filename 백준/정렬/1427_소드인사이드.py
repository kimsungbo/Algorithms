# 1427 소드인사이드
# 숫자정렬

number_list = (list(map(int, input())))
number_list = sorted(number_list)

ans = ''
for i in range(0, len(number_list)):
    ans = str(number_list[i]) + ans
    
print(ans)