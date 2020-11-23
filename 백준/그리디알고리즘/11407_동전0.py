# 11407 동전 0

n, k = map(int, input().split())

coin_list = []
for i in range(0, n):
    coin = int(input())
    # 가치의핪보다 비싼 동전은 필요없음으로 빼고 리스트에 넣어줌
    if(coin <= k):
        coin_list.append(coin)
        
remainder = k
product = 0

# 값이 큰 동전들부터 탐색 (값이 큰 동전들부터 써야 동전을 최소개로 쓸소 있음)
for i in range(len(coin_list)-1, -1, -1):
    
    if coin_list[i] <= remainder:
        product = product + (remainder // coin_list[i])
        remainder = remainder - ((remainder // coin_list[i]) * coin_list[i])
    
        if remainder == 0:
            break
        
print(product)