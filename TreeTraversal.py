def in_order_traverse_iterative(root):
    '''
    param: root is the root of the BST tree

    return a list of tree node
    '''
    node_list = []
    if root == None:
        return node_list
    node = root
    stack = [node]
    while node.left_child:
        node = node.left_child
        stack.append(node)
    while stack:
        node = stack.pop()
        #process
        node_list.append(node)
        if node.right_child:
            node = node.right_child
            stack.append(node)
            while node.left_child:
                node = node.left_child
                stack.append(node)
    return node_list

def in_order_traverse(root, node_list):
    '''
    in order traversal with recursion
    '''
    if root is None:
        return
    in_order_traverse(root.left_child, node_list)
    node_list.append(root)
    in_order_traverse(root.right_child, node_list)

class TreeNode:
    '''
    defintionof TreeNode for binary tree
    '''
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def test():
    '''
                 20
            -----|-------
            |           |
        |---15---|      40
        10      30
    '''
    root = TreeNode(20)
    left = TreeNode(15);right = TreeNode(40); root.left_child = left; root.right_child = right
    level3_left = TreeNode(10); level3_right = TreeNode(30); left.left_child = level3_left; left.right_child = level3_right
    #use recursion
    node_list = []
    in_order_traverse(root, node_list)
    for node

