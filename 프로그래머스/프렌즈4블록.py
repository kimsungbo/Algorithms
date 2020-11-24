def remove_block( m, n, board):
    
    remove_list = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] and board[i][j] != '*':
                remove_list.extend([[i+1, j], [i, j+1], [i+1, j+1], [i,j]])
                
    if len(remove_list) == 0:
        return -1
    
    else:
        for x, y in remove_list:
            board[x][y] = '*'
                
    

        
    while True:
        hasX = [False for i in range(m)]
        print(hasX)
        
        for i in range(m):
            if '*' in board[i]:
                hasX[i] = True
        
        done = True
        
        for i in range(m):
            if hasX[i] == False and True in hasX[i + 1:]:
                done = False
                break
                
        if all(hasX):
            for i in range(m):
                down(m, n, board)
        if done == True:
            return
        else:
            down(m, n, board)    


def down(m, n, board):
    for i in range(m-1, 0, -1):
        for j in range(n-1, -1, -1):
            if board[i][j] == '*' and board[i-1][j] != '*':
                temp = board[i-1][j]
                board[i][j] = temp
                board[i-1][j] = '*'

def solution(m, n, board):
    board = [list(row) for row in board]
    
    while True:
        temp = remove_block(m, n, board)
        
        if temp == -1:
            num_x = 0
            for i in range(m):
                for j in range(n):
                    if board[i][j] == '*':
                        num_x += 1
            return num_x