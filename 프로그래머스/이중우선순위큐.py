def solution(operations):
    queue = []
    for operation in operations:
        if operation[0] == 'I':
            queue.append(int(operation[2:]))
        elif operation[0] == 'D':
            if len(queue) == 0:
                continue
            else:
                queue.sort()
                if operation[2:] == '1':
                    queue.sort()
                    queue.pop()
                elif operation[2:] == '-1':
                    queue.pop(0)
    if not queue:
        return [0, 0]
    else:
        return [max(queue), min(queue)]