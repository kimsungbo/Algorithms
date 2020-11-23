def solution(n, words):
    
    for i in range(len(words)):
        if len(words[i]) == 1:
            return [i % n + 1, i // n]
        elif words[:i+1].count(words[i]) > 1:
            return [i % n + 1, i // n + 1]
        elif i != 0:
            if words[i-1][-1] != words[i][0]:
                return [i % n + 1, i // n + 1]
    return [0,0]