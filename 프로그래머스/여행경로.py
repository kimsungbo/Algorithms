from collections import deque
def dfs(tickets, graph):
    stack = deque(['ICN'])
    visited = ['ICN']
    
    num_airport = len(tickets) 
    
    while stack:
        current_airport = stack.popleft()
        
        if len(visited) == num_airport:
            visited.append(graph[current_airport][0])
            return visited
        
        print(graph)
        
        
        for next_airport in sorted((graph[current_airport])):
            print(current_airport, next_airport)
            print(graph)
            if next_airport in graph:
                if len(graph[next_airport]) != 0:
                    if [current_airport, next_airport] in tickets:
                        visited.append(next_airport)
                        print(next_airport, "appended")
                        stack.append(next_airport)
                        tickets.remove([current_airport, next_airport])
                        graph[current_airport].remove(next_airport)
                        break

    print(stack)
    return visited
            

def solution(tickets):
        
    graph = dict()
    
    for start, destination in tickets:
        if start in graph:
            graph[start].extend([destination])
        else:
            graph[start] = [destination]
            
    
    answer = dfs(tickets, graph)
    print(answer)
    return answer