# 1541 잃어버린 괄호
# 식의 값을 가능한 한 적게 만드는 문제

string = str(input())

# (-)기준으로 괄호를 쳐서 최솟값을 만든다
number_list = string.split('-')

for item in range(len(number_list)):
    add_list = list(map(int, number_list[item].split('+')))
    number_list[item] = sum(add_list)

ans = 0
number_list = list(map(int, number_list))
for i in range(len(number_list)):
    if i == 0:
        ans = ans + number_list[i]
    else:
        ans = ans - number_list[i]

print(ans)