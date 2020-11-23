def solution(phone_number):
    length = len(phone_number) - 4
    answer = '*' * length
    answer += phone_number[-4:]
    return answer