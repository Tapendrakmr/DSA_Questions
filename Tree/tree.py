class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Insert(self, data):
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.Insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.Insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=" ")
        if self.right:
            self.right.PrintTree()

    def Search(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.Search(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.Search(lkpval)
        else:
            return str(self.data) + ' is found'

    def inOrderTraversal(self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            # print(root.data)
            res.append(root.data)
            res = res+self.inOrderTraversal(root.right)
        return res

    def levelorderTraversal(self, root):
        que = []
        que.append(root)
        while len(que) > 0:
            x = que.pop(0)
            print(x.data, end=' ')
            if x.left:
                que.append(x.left)
            if x.right:
                que.append(x.right)

    def mirror(self, root):
        if root is None:
            return 0
        left = self.mirror(root.left)
        right = self.mirror(root.right)
        root.left = left
        root.right = right
        return root


value = int(input("Enter Root Node :"))
tree = Node(value)
t = int(input("Enter number of element :"))
for _ in range(t):
    e = int(input())
    tree.Insert(e)
# print("result")
# tree.PrintTree()
# print("InorderTraversal")
# print(tree.inOrderTraversal(tree))

# f = int(input("Enter the value you want to check :"))
# print(tree.Search(f))
print('levelorder')
tree.levelorderTraversal(tree)
print('mirror')
tree.mirror(tree)

print("modified levelorder")
tree.mirror(tree)
