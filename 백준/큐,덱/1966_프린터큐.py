# 1966 프린터 큐

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    
    queue = list(map(int, input().split()))

    
    #print(queue)

    idx = list(range(len(queue)))
    idx[m] = 'target'
    
#     print(idx)
    
    order = 0
    while True:
        if queue[0] == max(queue):
            order+=1
                
            if( idx[0] == 'target'):
                print(order)
                break
                
            else:

                x = queue.pop(0)
                idx.pop(0)
#                 print('pop', x)
                
        else:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))
            
#         print(idx)
#         print(queue)