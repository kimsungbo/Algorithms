def solution(msg):
    
    dictionary = {'A': 1, 'B' : 2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7,
                 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,
                  'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 
                  'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    
    index = 1
    answer = []
    letter = msg[0]
    count = 26
    
    while index < len(msg):

        if letter + msg[index] not in dictionary:
            answer.append(dictionary[letter])
            count += 1
            dictionary[letter + msg[index]] = count
            
            letter = msg[index]
            index +=1 
            
        else:
            letter += msg[index]
            index += 1

    answer.append(dictionary[letter])
    return answer
    