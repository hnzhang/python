class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinaryTree:
    '''
    '''
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    # Helper method
    def find_min(self,root):
        if root == None:
            return None
        if root.left_child == None:
            return root
        return self.find_min(root.left_child)
    
    def delete(self,root, data):
        # Return the new root node of type TreeNode
        if not root:
            return root
        if root.data == data:#delete me
            if root.right_child:
                new_root = self.find_min(root.right_child)
                if new_root == root.right_child:#new_root is a leaf node
                    new_root.left_child = root.left_child
                    new_root.right_child = None
                else:

                    #new_root can only possibly have right child
                    temp_ref = None
                    if new_root.right_child:
                        temp_ref = new_root.right_child
                    #find new_root's parent, and set its left child as temp_ref
                    node = root.right_child
                    while node.left_child != new_root:
                        node = node.left_child
                    node.left_child = temp_ref#break the link, and adjust the tree
                
                    new_root.left_child = root.left_child
                    new_root.right_child = root.right_child

                    root.left_child = None
                    root.right_child = None

                return new_root
            elif root.left_child:
                new_root = root.left_child
                root.left_child = None
                return new_root
            else:
                return None

        elif root.data > data:
            root.left_child = self.delete(root.left_child, data)
            return root
        else:
            root.right_child = self.delete(root.right_child, data)
            return root
    def find_path_to_node(self, root, data):
        if root is None:
            return None
        sub_paths = None
        if root.data == data:
            return [root]
        elif root.data > data:
            sub_paths = self.find_path_to_node(root.right_child, data)
        else:
            sub_paths = self.find_path_to_node(root.left_child, data)
        if sub_paths:
            return [root] + sub_paths
        else:
            return None

def test():
    root = TreeNode(9)
    root.left_child = TreeNode(3)
    root.left_child.left_child = TreeNode(2)
    root.left_child.left_child.left_child = TreeNode(1)
    root.left_child.right_child = TreeNode(4)
    root.left_child.right_child.right_child = TreeNode(5)
    bst= BinaryTree(root)
    bst.delete(root, 3)

def test_find_node_path():

