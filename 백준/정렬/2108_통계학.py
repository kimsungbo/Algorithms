# 2108 통계학

import sys

def mean(x):
    return round(sum(x)/len(x))

def median(x):
    if len(x) == 1:
        return (x[0])
    else:
        return (x[len(x) // 2])

from collections import Counter
def many_value(x):
    cnt = Counter(x)
    mod = cnt.most_common(2)
    
    if len(mod) > 1:
        if(mod[0][1] == mod[1][1]):
            return mod[1][0]
        else:
            return mod[0][0]
    else:
        return mod[0][0]

def minmax(x):
    return int(max(x) - min(x))

n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline())) 
num_list = sorted(num_list)

print(mean(num_list))
print(median(num_list))
print(many_value(num_list))
print(minmax(num_list))