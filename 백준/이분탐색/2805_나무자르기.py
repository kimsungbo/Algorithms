# 2805 나무 자르기

n, m = map(int, input().split())

tree_list = list(map(int, input().split()))


start = 1
end = max(tree_list)

while start <= end:
    mid = (start + end ) //2
    

    bring_home = 0
    
    for item in tree_list:
        if item >= mid:
            bring_home += (item - mid)
        
    if bring_home >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)