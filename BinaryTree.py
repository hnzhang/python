class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
class BinaryTreee:
    def __init__(self, root):
        self.root = root
    def find_path_to_node(self, root, data):
        if root is None:
            return None
        
        if root.data == data:
            return [root]
        
        paths = self.find_path_to_node(root.left_child, data)
        if not paths:
            paths = self.find_path_to_node(root.right_child, data)
        
        if paths:
            return [root] + paths
        else:
            return None
    def findLCA(self, root,node_a, node_b):
        path_a = self.find_path_to_node(root, node_a)
        path_b = self.find_path_to_node(root, node_b)
        LCA = None
        if path_a and path_b:
            for i in range(0, min(len(path_a), len(path_b))):
                if path_a[i] == path_b[i]:
                    LCA = path_a[i]
                else:
                    break
        return LCA

    def get_node_distance(self, root, node_data1, node_data2):
        path_to_node1 = self.find_path_to_node(root, node_data1)
        path_to_node2 = self.find_path_to_node(root, node_data2)

        print(path_to_node1)
        print(path_to_node2)
        node_distance = -1
        if path_to_node1 and path_to_node2:
            min_len = len(path_to_node1)
            if min_len > len(path_to_node2):
                min_len = len(path_to_node2)
            i = 0
            while i < min_len:
                if path_to_node1[i] != path_to_node2[i]:
                    break
                i += 1
            node_distance = len(path_to_node1[i:]) + len(path_to_node2[i:])
        return node_distance

def test():
    root = TreeNode(1)
    root.left_child = TreeNode(2)
    root.left_child.left_child = TreeNode(3)

    tree = BinaryTreee(root)
    print("distance:", tree.get_node_distance(root, 3, 1))
    print("LCA", tree.findLCA(root, 3, 1).data)

    root = TreeNode(1)
    root.left_child = TreeNode(2); root.right_child = TreeNode(3)
    root.left_child.left_child = TreeNode(4); root.left_child.right_child = TreeNode(5)
    root.right_child.left_child = TreeNode(6); root.right_child.right_child = TreeNode(7)
    tree = BinaryTreee(root)
    print("distance:", tree.get_node_distance(root, 4, 6))
    print("LCA", tree.findLCA(root, 4, 6).data)


test()
