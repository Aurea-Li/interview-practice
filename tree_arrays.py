# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def BSTSequences(r):
    current_array = []
    all_arrays = []
    valid_next = [r]

    BSTRecurse(all_arrays, current_array, valid_next)
    return all_arrays


def BSTRecurse(all_arrays, current_array, valid_next):

    if current_array:

        n = current_array[-1]
        if n.left:
            valid_next.append(n.left)
        if n.right:
            valid_next.append(n.right)

    if not valid_next:

        all_arrays.append([x.val for x in current_array])
        return

    else:
        for i in range(len(valid_next)):
            BSTRecurse(all_arrays, current_array + [valid_next[i]], valid_next[:i] + valid_next[i+1:])


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(6)

print(BSTSequences(root))
