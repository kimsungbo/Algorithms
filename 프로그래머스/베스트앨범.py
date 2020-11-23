import operator

def solution(genres, plays):
    most_played = dict()
    
    for i in range(len(genres)):
        if genres[i] in most_played:
            most_played[genres[i]][0] = most_played[genres[i]][0] + plays[i]
            most_played[genres[i]].append([plays[i], i])

        else:
            most_played[genres[i]] =  [plays[i]]
            most_played[genres[i]].append([plays[i], i])
            
                

    most_played = sorted(most_played.items(), key=operator.itemgetter(1), reverse=True)

    ans = []
    for genre, play in most_played:
        temp_array = play[1:]
        temp_array = sorted(temp_array, key = lambda x: (-x[0], x[1]))
        
        if len(temp_array) == 1:
            ans.append(temp_array[0][1])
        else:
            ans.append(temp_array[0][1])
            ans.append(temp_array[1][1])
        
    return ans