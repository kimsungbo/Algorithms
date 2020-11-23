# 1018 체스판 다시 칠하기
# 체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제

start_w = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

start_b =[['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

n, m = map(int, input().split())

board = []
for x in range(0, n):
    board.append(list(str(input())))
    
def compare_board(start_w, start_b, board):
    count_w = 0
    count_b = 0
    
    for i in range(0, 8):
        for j in range(0, 8):
            if(board[i][j] != start_w[i][j]):
                count_w += 1
            if(board[i][j] != start_b[i][j]):
                count_b += 1
    return min(count_w, count_b)

num_change_list = []

for i in range(0, n - 7):
    for j in range(0, m  - 7):
        new_board = []
        new_board.append(board[i][j:j+8])
        new_board.append(board[i+1][j:j+8])
        new_board.append(board[i+2][j:j+8])
        new_board.append(board[i+3][j:j+8])
        new_board.append(board[i+4][j:j+8])
        new_board.append(board[i+5][j:j+8])
        new_board.append(board[i+6][j:j+8])
        new_board.append(board[i+7][j:j+8])
        
        num_change_list.append(compare_board(start_w, start_b, new_board))
        
print(min(num_change_list))