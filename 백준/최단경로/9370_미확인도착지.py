# 9370 미확인 도착지
# 최단거리 알고리즘 응용 문제

#9370 미확인 도착지

import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize - 3000

T = int(input())
    

def Dijkstra(start):
    heap=[]
    # 시작점에서 자기 자신까지는 가중치 0
    dp = [INF] * (n+1)
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        
        currentWeight, currentNode = heapq.heappop(heap)
        
        # 현재 가중치 테이블과 비교하여 더 큰 가중치면 무시
        if dp[currentNode] < currentWeight:
            continue
            
        for tempWeight, nextNode in graph[currentNode]:
            nextWeight = tempWeight + currentWeight
            # 다음 노드까지의 가중치가 현재 기록된 가중치보다 작으면 조건 성립
            if nextWeight < dp[nextNode]:
                # 가중치 테이블 업데이트
                dp[nextNode] = nextWeight
                # 다음 점까지의 가중치와 다음 점에 대한 튜플을 묶어 힙에 저장
                heapq.heappush(heap, (nextWeight, nextNode))
        
    return dp
           

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    HtoG = 0
    
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
        
        # 꼭 지나가야 하는 도로의 가중치 저장해놓기
        if (a == h and b == g) or (a == g and b == h):
            HtoG = d
        
        
    dest = []
    
        
    for _ in range(t):
        dest.append(int(input()))
        
    min_dis = []

       
    for i in range(len(dest)):
        
        S = Dijkstra(s)
        G = Dijkstra(g)
        H = Dijkstra(h)

        minimum = min(S[h] + HtoG + G[dest[i]], S[g] + HtoG + H[dest[i]])
        
        # 시작점에서 바로간것보다 더 오래걸리면 최종 목적지가 아님
        if minimum == S[dest[i]]:
            min_dis.append(dest[i])
            
    print(*sorted(min_dis))