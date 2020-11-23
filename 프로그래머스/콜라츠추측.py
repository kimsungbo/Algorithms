def solution(num):
    
    count = 0
    while True:
        if num == 1:
            return count
        if count == 500 and num != 0:
            return -1

        if num % 2 == 0:
            num = num // 2
        elif num % 2 != 0:
            num = (num*3) + 1
        count += 1