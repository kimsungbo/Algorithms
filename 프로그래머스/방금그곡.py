from datetime import datetime

def replace_sharp(string):
    string = string.replace('C#', 'c')
    string = string.replace('D#', 'd')
    string = string.replace('F#', 'f')
    string = string.replace('G#', 'g')
    string = string.replace('A#', 'a')
    
    return string
    
def solution(m, musicinfos):
    
    m = replace_sharp(m)
    answer_list = []
    
    for music in musicinfos:
        rhythm = replace_sharp(music.split(',')[-1])
        title = music.split(',')[-2]
        t1 = music.split(',')[0]
        t2 = music.split(',')[1]
        
        FMT = '%H:%M'
        tdelta = str(datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT))
        
        tdelta = tdelta.split(' ')[-1]
        tdelta = tdelta.split(':')
        tdelta = [int(i) for i in tdelta]
        
        time = 0
        time += tdelta[0] * 60 + tdelta[1]

        
        for i in range(1, time // len(rhythm) + 1):
            rhythm += replace_sharp(music.split(',')[-1])
            
        rhythm = rhythm[:time]

        if m in rhythm:
            answer_list.append([time, title])

    if len(answer_list) == 0:
        return "(None)"
    
    elif len(answer_list) == 1:
        return answer_list[0][-1]

    else:
        answer_list = sorted(answer_list, key = lambda x: x[0], reverse=True)
        return answer_list[0][-1]
        