# 1037 약수

n = int(input())

factor_list = sorted(list(map(int, input().split())))

print(factor_list[0] * factor_list[-1])