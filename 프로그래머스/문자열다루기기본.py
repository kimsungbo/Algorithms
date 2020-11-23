def solution(s):
    try:
        s = int(s)
        s = str(s)
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    except:
        return False