# 1931 회의실 배정
# 가능한 한 많은 구간을 선택하는 문제

n = int(input())

meeting_list = []
for i in range(n):
    x, y = map(int, input().split())
    meeting_list.append([x, y])
    
# 가장 많은 회의를 하기 위해서는 빨리 끝나는 회의순으로 정렬해야함
# 빨리 끝나는 회의일수록 뒤에 고려할수 있는 회의가 많아짐
meeting_list = sorted(meeting_list, key = lambda x : (x[1], x[0]))


possible_meetings = []
end_time = 0
for i in range(len(meeting_list)):
    
    if i == 0:
        possible_meetings.append(meeting_list[i])
        end_time = meeting_list[i][1]
    else:
        if meeting_list[i][0] >= end_time:
            possible_meetings.append(meeting_list[i])
            end_time = meeting_list[i][1]
    
print(len(possible_meetings))