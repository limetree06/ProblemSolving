"""
이진트리 순회 연습

    1    
  2    3
4  5  6  7

       D(1)         D(1) -> 부모 * 2 -> D(2)
   D(2)     D(3)    D(1) -> 부모 * 2 + 1 -> D(3)
D(4) D(5) D(6) D(7)

이런 트리가 있을 때 
preorder Traversal : 1 - 2 - 4 - 5 - 3 - 6 - 7 (root 먼저하고 왼쪽, 오른쪽 방문)
inorder Traversal : 4 - 2 - 5 - 1 - 6 - 3 -7 (왼쪽 - root - 오른쪽 출력)
postorder Traversal : 4 - 5 - 2 - 6 - 7 - 3 - 1 (왼쪽 - 오른쪽 - root 출력)
Levelorder Traversal
재귀로 풀어보기  
    
"""

# print의 위치에 동작해야하는 코드들이 들어가는 것.
# print의 위치에 따라 preorder, inorder, postorder들이 정해진다!


def preorder(node):
    if node > 7:
        return
    else:
        print(node, end=" ")
        preorder(node * 2)
        preorder(node * 2 + 1)


def inorder(node):
    if node > 7:
        return
    else:
        preorder(node * 2)
        print(node, end=" ")
        preorder(node * 2 + 1)


def postorder(node):
    if node > 7:
        return
    else:
        preorder(node * 2)
        preorder(node * 2 + 1)
        print(node, end=" ")


preorder(1)
print("\n")
inorder(1)
print("\n")

postorder(1)
