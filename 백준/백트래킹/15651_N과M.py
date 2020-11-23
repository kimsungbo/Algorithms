# 15651 N과 M
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다

n, m = map(int, input().split())

num_list = list(range(1, n+1))


from itertools import product
combi = product(num_list, repeat=m)

for comb in combi:
    for i in range(0, m):
        print(comb[i], end=" ")
    print()