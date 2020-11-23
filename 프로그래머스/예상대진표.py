def solution(n,a,b):
    
    players = [i for i in range(1, n+1)]
    
    count = 1
    
    while True:
        new_players = []
        for i in range(0, len(players) -1, 2):
            x = players[i]
            y = players[i+1]
            
            if (x == a and y == b) or (x == b and y == a):
                return count            
            elif x == a or y == a:
                new_players.append(a)
            elif x == b or y == b:
                new_players.append(b)
            else:
                new_players.append(x)
                
        count += 1
        players = new_players

