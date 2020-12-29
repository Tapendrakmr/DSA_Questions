from collections import defaultdict


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printPreorder(root):
    # Recursive
        # if root:
        #     print(root.val)
        #     printPreorder(root.left)
        #     printPreorder(root.right)

    # Iterative
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        print(curr.val, end=' ')
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)


def printPostorder(root):
    # Recursive
    # if root:
    #     printPostorder(root.left)
    #     printPostorder(root.right)
    #     print(root.val)

    # Iterative

    stack = []
    stack.append(root)
    out = []
    while stack:
        curr = stack.pop()
        out.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
        while out:
            print(out.pop())


def InorderTraversal(root):
    # Recursive
    # if root == None:
    #     return None
    # InorderTraversal(root.left)
    # print(root.val, end=" ")
    # InorderTraversal(root.right)

    # Iterative
    stack = []
    res = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            # print(curr.val)
            res.append(curr.val)
            curr = curr.right
    return res


def levelOrderTraversal(root):
    queue = []
    queue.append(root)
    while len(queue) > 0:
        x = queue.pop(0)
        print(x.val)
        if x.left:
            queue.append(x.left)
        if x.right:
            queue.append(x.right)


def height(root):
    if root is None:
        return 0
    else:
        left = height(root.left)
        right = height(root.right)
        return 1+max(left, right)


def diameter(root):
    if root is None:
        return 0
    leftheight = height(root.left)
    rigtheight = height(root.right)

    leftDiameter = diameter(root.left)
    rigtDiameter = diameter(root.right)
    return max(leftheight+rigtheight, max(leftDiameter, rigtDiameter))


def Mirror(root):
    if root is None:
        return root
    left = Mirror(root.left)
    right = Mirror(root.right)
    root.left = right
    root.right = left
    return root


def LeftView(root):
    if not root:
        return
    q = []
    q.append(root)
    while (len(q)):
        n = len(q)
        for i in range(1, n+1):
            temp = q[0]
            q.pop(0)
            if i == 1:
                print(temp.val, end=' ')
            if(temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)


def RightView(root):
    if not root:
        return
    q = []
    q.append(root)
    while (len(q)):
        n = len(q)
        for i in range(1, n+1):
            temp = q[0]
            q.pop(0)
            if i == n:
                print(temp.val, end=' ')
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)


def TopView(root):
    if root is None:
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd
    q.append(root)
    while (len(q)):
        root = q[0]
        hd = root.hd
        if hd not in m:
            m[hd] = root.val
        if root.left:
            root.left.hd = hd-1
            q.append(root.left)
        if root.right:
            root.right.hd = hd+1
            q.append(root.right)
        q.pop(0)
    print(m)
    for i in sorted(m):
        print(m[i], end=" ")


def BottomView(root):
    if root is None:
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd
    q.append(root)
    while (len(q)):
        root = q[0]

        hd = root.hd
        m[hd] = root.val
        if root.left:
            root.left.hd = hd-1
            q.append(root.left)
        if root.right:
            root.right.hd = hd+1
            q.append(root.right)
        q.pop(0)

    for i in sorted(m):
        print(m[i], end=' ')

# To check balanced Tree


def getheight(root):
    if root is None:
        return 0
    l = getheight(root.left)
    r = getheight(root.right)
    if l == -1 or r == -1 or abs(l-r) > 1:
        return -1
    return max(l, r)+1


def heightBalanced(root):
    if root is None:
        return True
    if (getheight(root) != -1):
        return "True"
    else:
        return "False"


def printDiagnole(root):
    if root is None:
        return
    m = defaultdict(list)
    hd = 0
    root.hd = hd
    q = []
    q.append(root)
    while len(q):
        root = q[0]
        hd = root.hd
        m[hd].append(root.val)
        if root.left:
            root.left.hd = hd+1
            q.append(root.left)
        if root.right:
            root.right.hd = hd
            q.append(root.right)
        q.pop(0)
    print(m)


def sumTree(root):
    if root is None:
        return 0
    old = root.val
    root.val = sumTree(root.left)+sumTree(root.right)
    return root.val+old


def maxSumPath(root):
    if root is None:
        return 0
    ls = maxSumPath(root.left)
    rs = maxSumPath(root.right)
    return max(ls, rs)+root.val
# Find largest subtree sum in a tree


def findlargestSubtreeSumUtil(root, ans):
    if root is None:
        return 0
    cur = root.val + \
        findlargestSubtreeSumUtil(root.left, ans) + \
        findlargestSubtreeSumUtil(root.right, ans)
    ans[0] = max(ans[0], cur)
    return cur


def findlargestSubtreeSum(root):
    if root is None:
        return 0
    ans = [-999999999]
    findlargestSubtreeSumUtil(root, ans)
    return ans[0]

# find path


def pathpreorder(root, sum, k, path, finalarr):
    if root is None:
        return
    sum += root.val
    # print(sum)
    path.append(root.val)
    if sum == k:
        finalarr.append(path)
        print(path)

    pathpreorder(root.left, sum, k, path, finalarr)
    pathpreorder(root.right, sum, k, path, finalarr)
    sum -= path[-1]
    path.pop(-1)


def pathSum(root, k):
    path = []
    sum = 0
    finalarr = []
    pathpreorder(root, sum, k, path, finalarr)

# Lowest common ancestor


def commonAncestor(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root

    left = commonAncestor(root.left, p, q)
    right = commonAncestor(root.right, p, q)
    if left is not None and right is not None:
        return root
    if left is None and right is None:
        return None
    if left is not None:
        return left
    else:
        return right
# find distance between 2 node


def findLevel(root, data, d, level):  # find distacne
    if root is None:
        return
    if root.val == data:
        d.append(level)
        return
    findLevel(root.left, data, d, level+1)
    findLevel(root.right, data, d, level+1)


def findDistance(root, n1, n2):
    lca = commonAncestor(root, n1, n2)
    d1 = []  # distance for n1
    d2 = []  # distance for n2
    if lca:
        findLevel(lca, n1, d1, 0)
        findLevel(lca, n2, d2, 0)
        return d1[0]+d2[0]
    else:
        return -1

# print ancestore of node


def printAncestor(root, node, k):
    if root is not None:
        if root.val == node or printAncestor(root.left, node, k) or printAncestor(root.right, node, k):
            #    print all ancestor
            print(root.val, " ", k[0])
            k[0] = k[0]-1
            return 1
        # print specific number of ancestor
            # if k == 0:
            #     print(root.val)
            #     return 0
            # k = k-1
            # return 1
    return 0
# convert binary tree to binay search tree


def convertToBST(root):
    if root is None:
        return root
    inorderArr = InorderTraversal(root)
    inorderArr.sort()
    i = 0
    curr = root
    stack = []
    if root:
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr.val = inorderArr[i]
                i += 1
                curr = curr.right


root = Node(20)

root.left = Node(8)
root.right = Node(22)
root.right.right = Node(25)
root.left.left = Node(5)
root.left.left.left = Node(-2)
root.left.left.right = Node(9)
root.left.right = Node(3)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
# print("print preorder")

# printPreorder(root)
# printPostorder(root)
# levelOrderTraversal(root)
# print(height(root))
# print("befor modification")
# print(InorderTraversal(root))
# M = Mirror(root)
# print("after Modification")
# print(InorderTraversal(M))

# # print iterative Inorder
# InorderTraversal(root)

# LeftView(root)
# RightView(root)
# TopView(root)
# BottomView(root)

# print(heightBalanced(root))
# printDiagnole(root)

# print("before sum tree")
# InorderTraversal(root)
# sumTree(root)

# print("After sum Tree")
# InorderTraversal(root)

# print(maxSumPath(root))

# print(findlargestSubtreeSum(root))
# pathSum(root, 41)
# commonAncestor(root, 22, 8)
# printAncestor(root, 5, [2])

# Inorder Traversal
print(InorderTraversal(root))
convertToBST(root)
print(InorderTraversal(root))
