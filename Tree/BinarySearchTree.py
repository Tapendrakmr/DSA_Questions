class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)
# Delete Node


def minValueNode(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def search(root, key):
    if root is None or root.val == key:
        return print("value exist")

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


# def deleteNode(root, key):
#     if root is None:
#         return root
#     if key < root.val:
#         root.left = deleteNode(root.left, key)
#     elif key > root.val:
#         root.right = deleteNode(root.right, key)
#     else:
#         if root.left is None:
#             temp = root.right
#             root = None
#             return temp
#         elif root.right is None:
#             temp = root.left
#             root = None
#             return temp
#         temp = minValueNode(root.right)

#         root.val = temp.val
#         root.rigt = deleteNode(root.right, temp.val)
#     return root


def deleteNode(root, key):

    if root is None:
        return root

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.val):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root


def minAndMax(root):
    current = root
    min, max = 99999, -99999
    while current.left is not None:
        current = current.left
    min = current.val
    current = root
    while current.right is not None:
        current = current.right
    max = current.val
    return print("min value :", min, " max value :", max)
# InorderTraversal


def InorderTraversal(root):
    if root is None:
        return root

    stack = []
    res = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr)
            curr = curr.right
    return res


def preoderTraversal(root):
    if not root:
        return
    print(root.val)
    preoderTraversal(root.left)
    preoderTraversal(root.right)


def inorderPredecesssor(root, key, pre, suc):
    if root == None:
        return

    while root != None:
        if root.val == key:
            if root.left:
                pre[0] = root.left
                while pre[0].right:
                    pre[0] = root.right
            if root.right:
                suc[0] = root.right
                while suc[0].left:
                    suc[0] = suc[0].left
            return

        elif root.val < key:
            pre[0] = root
            root = root.right
        else:
            suc[0] = root
            root = root.left

    return
# Check tree is bst or not


def checkBST(root, min, max):
    if root is None:
        return True
    if ((root.left is not None and root.left.val < min) or (root.right is not None and root.right.val > max)):
        return False
    return checkBST(root.left, min, root.val) and checkBST(root.right, root.val, max)

# find lca


def lca(root, n1, n2):
    while root:
        if root.val < n1 and root.val < n2:
            root = root.right
        elif root.val > n1 and root.val > n2:
            root = root.left
        else:
            break
    return root.val
# convert bst to balanced bst


def buildTree(array, start, end):
    if start > end:
        return None
    middle = (start+end)//2
    node = array[middle]
    node.left = buildTree(array, start, middle-1)
    node.right = buildTree(array, middle+1, end)
    return node


def BalancedBSt(root):
    if root is None:
        return root
    inorderArr = InorderTraversal(root)
    size = len(inorderArr)
    return buildTree(inorderArr, 0, size-1)

# merge two binary tree


def merge(root1, root2):
    if root1 is None and root2 is None:
        return None
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    else:
        arr = InorderTraversal(root1)+InorderTraversal(root2)
        # print("first \n ", arr)
        arr.sort(key=lambda x: x.val)
        # print("Second \n", arr)
        size = len(arr)
        start = 0
        return buildTree(arr, start, size-1)

# KTh largest element in BST


def kthLargest(root, k):
    if root is None or k < 1:
        return None
    curr = root
    stack = []
    res = 0
    while (curr or stack) and k > 0:

        if curr:
            stack.append(curr)
            curr = curr.right
        else:

            curr = stack.pop()
            res = curr.val
            curr = curr.left
            k -= 1
    if k == 0:
        print(res)
        return res
    return None
# kth minimum element


def KthMinimum(root, k):
    if root is None or k < 1:
        return None
    curr = root
    stack = []
    while (stack or curr) and k > 0:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res = curr.val
            curr = curr.right
            k -= 1
    if k == 0:
        print(res)
        return res
    return None


# nodes lies in a range
def getRange(root, low, high):
    if root is None:
        return 0
    if root.val <= high and root.val >= low:
        return 1+(getRange(root.left, low, high)+getRange(root.right, low, high))
    elif root.val < low:
        return getRange(root.right, low, high)
    else:
        return getRange(root.left, low, high)


# Tree1
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print(getRange(r, 90, 110))


# print(kthLargest(r, 1))
# print(KthMinimum(r, 1))
# Tree2
# r2 = Node(10)
# r2 = insert(r2, 8)
# r2 = insert(r2, 7)
# r2 = insert(r2, 6)
# r2 = insert(r2, 5)
# # Merge 2 binary Search tree
# root = merge(r, r2)
# preoderTraversal(root)
# search(r, 20)
# print("before delete")
# inorder(r)

# deleteNode(r, 30)
# print("After delete")
# inorder(r)

# print("Min and max element in treee")
# minAndMax(r)

# print("Inorder Predecessor")
# pre, suc = [None], [None]
# inorderPredecesssor(r, 70, pre, suc)
# print(pre[0].val, suc[0].val)

# print("tree is bst or not")
# if checkBST(r, -9999, 9999) is True:
#     print("Given Tree is Bst")
# else:
#     print("")

# print("lowest common ancestor")
# print(lca(r, 30, 20))
# root = BalancedBSt(r)
# preoderTraversal(root)

# print kth largest element
# print(kthLargest(r, 3))
