"""
Tree Traversals
Inorder: inorder left, root, inorder right
PreOrder: root first, recursive preorder left, recursive right
PostOrder: left first, right next, root last

"""


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()
#Beter to implement outside the tree, this is not ideal


def postorder(self):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
        
def inorder(self):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootChild())
        inorder(tree.getRightChild())
