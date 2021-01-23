"""
Class definition for a Binary Tree Node
"""
class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

"""
Tree class for handing note creation and other common methods
"""
class Tree:
    def createNode(self, data):
        return BinaryTreeNode(data)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end = " ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.inorder(root.left)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.data, end = " ")

    def insert(self, root, data):
        newNode = self.createNode(data)
        if root is None:
            return newNode
        else:
            queue = []
            queue.append(root)
            while (len(queue) != 0):
                current = queue[0]
                queue.pop()
                if not current.left:
                    current.left = newNode
                    return
                else:
                    queue.append(current.left)
                if not current.right:
                    current.right = newNode
                    return
                else:
                    queue.append(current.right)

    def delete(self, root, value):
        def deleteDeepestNode(root, deepest_node):
            q = []
            q.append(root)
            while q:
                tmp = q.pop()
                if tmp is deepest_node:
                    tmp = None
                    return

                if tmp.right:
                    if tmp.right is deepest_node:
                        tmp.right = None
                        return
                    else:
                        q.append(tmp.right)

                if tmp.left:
                    if tmp.left is deepest_node:
                        tmp.left = None
                        return
                    else:
                        q.append(tmp.left)

        if not root:
            return None
        if not root.left or not root.right:
            if root.data == value:
                return None
            else:
                return root

        queue = []
        queue.append(root)
        matchingNode = None
        while queue:
            temp = queue.pop()
            if temp.data == value:
                matchingNode = temp
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        if matchingNode:
            x = temp.data
            deleteDeepestNode(root, temp)
            matchingNode.data = x
        return root

    def printTree(self, root, level=0):
        if root != None:
            self.printTree(root.right, level + 1)
            print(' ' * 4 * level + '->', root.data)
            self.printTree(root.left, level + 1)


tree = Tree()
root = tree.createNode(4)

tree.insert(root, 7)
tree.insert(root, 8)
tree.insert(root, 3)

tree.inorder(root)
print('\n')
tree.printTree(root)
print('\n')
tree.postorder(root)
print('\n')
tree.preorder(root)
print('\n')
tree.delete(root,7)
print('\n')
tree.printTree(root)
