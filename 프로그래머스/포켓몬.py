def solution(nums):
    
    if len(set(nums)) <= len(nums) // 2:
        return len(set(nums))
    else:
        return len(nums) // 2
    
    answer = 0
    return answer