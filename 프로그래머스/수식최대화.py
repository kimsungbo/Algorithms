def calculate(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    
    if priority[n] == '*':
        res = eval('*'.join([calculate(priority, n+1, e) for e in expression.split('*')]))
    elif priority[n] == '+':
        res = eval('+'.join([calculate(priority, n+1, e) for e in expression.split('+')]))
    elif priority[n] == '-':
        res = eval('-'.join([calculate(priority, n+1, e) for e in expression.split('-')]))
    return str(res)


        
        
def solution(expression):
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    
    answer = 0
    for priority in priorities:
        res = int(calculate(priority, 0, expression))
        answer = max(abs(res), answer)
    return answer