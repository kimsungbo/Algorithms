# 1874 스택수열

n = int(input())

stack = []
operation = []
possible = True
count = 1

for i in range(n):
    num_to_pop = int(input())
    
    while count <= num_to_pop:
        stack.append(count)
        operation.append('+')
        count+= 1
    
    if(stack[-1] == num_to_pop):
        stack.pop()
        operation.append('-')
    else:
        possible = False
            
if possible == False:
    print("NO")
else:
    for op in operation:
        print(op)