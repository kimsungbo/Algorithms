def solution(n, results):
    win = dict()
    lose = dict()
    
    for i in range( 1, n + 1):
        win[i] = set()
        lose[i] = set()
        

    
    for a, b in results:
        win[a].add(b)
        lose[b].add(a)   
    
    print(win)
    print(lose)
    
    for i in range(1, n+1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])

    print(win)
    print(lose)   


    count = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            count += 1
    return count