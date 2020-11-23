# 7568 덩치
# 모든 사람을 비교하여 덩치 등수를 구하는 문제

x = int (input())

people = {}
for i in range(0,x):
    height, weight = map(int, input().split())
    people[i] = {'weight' : weight, 'height' : height, 'rank' : 0}
    
for k in people:
    count = 0
    for i in range(0, x):
        if i != k:
            if (people[k]['weight'] < people[i]['weight'] and people[k]['height'] < people[i]['height']):
                count+=1
    people[k]['rank'] = count+1
        
for k in people:
    print(people[k]['rank'], end=" ")