# 2263 트리의 순회
# 중위 순회와 후위 손회가 주어졌을 때 전위 순회를 구하는 문제

import sys
sys.setrecursionlimit(10**6)


n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)

for i in range(n):
    pos[inorder[i]] = i
    
    

def divide(in_start, in_end, post_start, post_end):
    
    if(in_start > in_end) or (post_start > post_end):
        return
    
    root = postorder[post_end]

    print(root, end=" ")
    
    p = pos[root] 
    
    left = p- in_start
    
    divide(in_start, p - 1, post_start, post_start + left - 1)
    divide(p + 1, in_end, post_start + left, post_end - 1)

divide(0, n-1, 0, n-1)
