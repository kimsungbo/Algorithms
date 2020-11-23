import heapq
def solution(jobs):
    answer = 0
    length = len(jobs)
    jobs.sort()
    # 젤 처음에 요청된 작업부터 처리 시작
    start = jobs[0][0]
    heap = []
    
    while jobs:
        requested, consumed = jobs.pop(0)
        start += consumed
        answer += (start - requested)
        
        # 요청된 작업을 처리하는동안 들어온 다른 요청들을 min heap 에 저장
        while jobs and jobs[0][0] < start:
            requested, consumed = jobs.pop(0)
            heapq.heappush(heap, (-consumed, requested))
            
        # 요청된 작업을 처리하는동안 들어온 요청들중 작업의 소요시간이 젤 작은 요청을 다음 작업으로 실시
        while heap:
            consumed, requested = heapq.heappop(heap)
            jobs.insert(0, [requested, -consumed])
            
            
    answer = answer // length
    return answer