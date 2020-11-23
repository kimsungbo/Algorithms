def solution(numbers, hand):
    board = {1: (0, 0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1),
            9:(2,2), -1: (3,0), 0: (3,1), -2:(3,2)}
    
    answer = ''
    current_left = -1
    current_right = -2
    for number in numbers:
        if number in [1, 4, 7] or current_left == number:
            answer += 'L'
            current_left = number
        elif number in [3, 6, 9] or current_right == number:
            answer += 'R'
            current_right = number
        else:
            left_d = abs(board[current_left][0] - board[number][0]) + abs(board[current_left][1] - board[number][1])
            right_d = abs(board[current_right][0] - board[number][0]) + abs(board[current_right][1] - board[number][1])
            
            if left_d == right_d:
                if hand == "right":
                    answer += "R"
                    current_right = number
                elif hand == "left":
                    answer += "L"
                    current_left = number
            elif left_d > right_d:
                answer += "R"
                current_right = number
            elif left_d < right_d:
                answer += "L"
                current_left = number
                
    return answer