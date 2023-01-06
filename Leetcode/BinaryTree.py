class Node:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.value}'


def add(root, n):
    if not root:
        return Node(n)
    if root.value > n:
        root.left = add(root.left, n)
    else:
        root.right = add(root.right, n)
    return root


def pre_order(root):
    if not root:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value)


l = [10, 30, 15, 5, 8, 14, 18, 28, 29, 50]
root = Node(25)
for i in l:
    add(root, i)

# pre_order(root)
post_order(root)
'''
          25
       /     \
     10       30     
    /  \     /  \
   5   15   28   50

'''