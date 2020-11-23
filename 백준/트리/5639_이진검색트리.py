# 5639 이진 검색 트리
# 이진 검색 트리의 전위 순회가 주어졌을때 후위 순회를 구하는 문제

# 이진 검색 트리
import sys
input = sys.stdin.readline

sys.setrecursionlimit(20_000)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if (self.root is None):
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if current.value > value:
                    if current.left == None:
                        current.left = Node(value)
                        break
                    else:
                        current = current.left
                elif current.value < value:
                    if current.right == None:
                        current.right = Node(value)
                        break
                    else:
                        current = current.right
                        
    def postorder(self, node):
        if node.left != None:
            self.postorder(node.left)
        if node.right != None:
            self.postorder(node.right)
        print(node.value)
   

bst = BinarySearchTree()


while True:
    try:
        bst.insert(int(input()))
    except:
        break
    
bst.postorder(bst.root)