def solution(numbers, target):
    
    tree = [0]
    
    for i in numbers:
        nodes = []
        for j in tree:
            nodes.append(j+i)
            nodes.append(j-i)
            
        tree = nodes
        
    return tree.count(target)