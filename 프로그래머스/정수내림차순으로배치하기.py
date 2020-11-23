def solution(n):
    n = str(n)
    n = [int(n[i]) for i in range(len(n))]
    n = sorted(n, reverse=True)
    n = [str(n[i]) for i in range(len(n))]
    return int(''.join(n))