import re

def solution(files):
    files = [re.split(r"([0-9]+)", file) for file in files]
    print(files)
    
    files = sorted(files, key = lambda x: (x[0].lower(), int(x[1])))
    print(files)
    
    return [''.join(file) for file in files]