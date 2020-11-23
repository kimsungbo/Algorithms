import copy

def solution(phone_book):
    phone_book = [int(phone_book[i]) for i in range(len(phone_book))]
    phone_book.sort()
    
    for num in phone_book:
        temp_book = copy.deepcopy(phone_book)
        temp_book.remove(num)
        
        temp_book = [str(temp_book[i])[:len(str(num))] for i in range(len(temp_book))]
        print(temp_book)

        if str(num) in temp_book:
            return False
    return True