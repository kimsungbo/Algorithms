# 11725 트리의 부모 찾기
# 루트가 1인 트리가 주어질 때, 각 노드의 부모를 구하는 문제

from collections import deque
import sys
n = int(input())

tree = dict()
tree = [set([]) for _ in range(n+1)]


for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].add(b)
    tree[b].add(a)

parents = [[] for _ in range(n + 1)]

def dfs(graph_list, start, parent):
    stack = [start]
    
    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
            
    return parent

for i in list(dfs(tree, 1, parents))[2:]:
    print(i[0])