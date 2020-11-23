# 2839 설탕 배달
# 5와 3을 최소 횟수로 합하여 N을 만드는 문제

x = int(input())

ans = -1

# 5로 나눠질 경우 5kg 봉지만 사용하는게 최소
if(x % 5 == 0):
    ans = int(x/5)
    

else:
    # 최대 x/3봉지까지만 사용되기때문에 x/3까지 루프
    for i in range(0, int(x / 3)):
        if(int((x - (i*3)) % 5 == 0)):
            ans = (i + int((x - (i*3)) / 5))
            break
        elif(x % 3 == 0):
            ans = x // 3
    
print(ans)