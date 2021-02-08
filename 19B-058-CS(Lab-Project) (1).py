class Node:
    def __init__(self, value):
        self.value = value
        self.Right = None
        self.Left = None


class Random_BST:
    def __init__(self):
        self.root = None

    def Insert(self, value):# insert function for to add valu in tree
        self.root = self.__Insert(self.root, value)
        

    def __Insert(self, root, value):
        if root is None:
            root = Node(value)
        else:
            if root.value > value:
                root.Left = self.__Insert(root.Left, value)
            else:
                root.Right = self.__Insert(root.Right, value)
        return root

    # LVR
    def InOrder(self):
        return self.__InOrder(self.root)

    def __InOrder(self, root):
        if root:
            self.__InOrder(root.Left)
            print(root.value)
            self.__InOrder(root.Right)

    # VLR
    def Preorder(self):
        return self.__preorder(self.root)

    def __preorder(self, root):
        if root:
            print(root.value)
            self.__preorder(root.Left)
            self.__preorder(root.Right)

    # LRV

    def PostOrder(self):
        return self.__PostOrder(self.root)

    def __PostOrder(self, root):
        if root:
            self.__PostOrder(root.Left)
            self.__PostOrder(root.Right)
            print(root.value)

    def isempty(self):
        if self.root is None:
            return True
        return False

    def Height(self):
        return self.__Height(self.root)

    def __Height(self, root):
        if root:
            left_height = self.__Height(root.Left)
            right_height = self.__Height(root.Right)
            return 1 + max(left_height, right_height)
        return 0

    def FindMax(self):#extra function max value in tree
        return self.__FindMax(self.root)

    def __FindMax(self, root):
        while root.Right:
            root = root.Right
        return root

    def FindMin(self):#finding min value in the tree
        return self.__FindMin(self.root)

    def __FindMin(self, root):
        while root.Left:
            root = root.Left
        return root

    def Successor(self):
        return self.__Successor(self.root)

    def __Successor(self, root):
        if root.Right:
            return self.__FindMin(root.Right)
        return None

    def Predecessor(self):
        return self.__Predecessor(self.root)

    def __Predecessor(self, root):
        if root.Left:
            return self.__FindMax(root.Left)
        return None

    def Delete(self, value):#Delete function for RBST
        return self.__Delete(self.root, value)

    def __Delete(self, root, value):
        if root is None:
            return root

        if value > root.value:
            root.Right = self.__Delete(root.Right, value)#cheching roots 

        elif value < root.value:
            root.Left = self.__Delete(root.Left, value)

        else:
            if root.Left is None:
                temp = root.Right
                root = None
                return temp

            elif root.Right is None:
                temp = root.Left
                root = None
                return temp

            else:
                temp = self.__FindMin(root.Right)
                root.value = temp
                root.Right = self.__Delete(root.Right, temp)

        return root
#A rotation in a binary search tree is a local modification that takes a parent u of anode w and makes w the parent of u, while preserving the binary searchtree property.
    def rotate_left(self,u):# if parent have right child then we use left rotation 
        w = u.Right
        w.parent = u.parent
        if w.parent != None:
            if w.parent.Left == u:#checking out parent is greater then child or not 
                w.parent.Left = w
            else:
                w.parent.Right = w
        u.Right = w.Left
        if u.Right != None :
            u.Right.parent = u
            u.parent = w
            w.Left = u
        if u == self.root :
            self.root = w
            self.root.parent = None

    def rotate_right(self,u):# if parent have left child then we use right rotation 
        w = u.Left
        w.parent = u.parent
        if w.parent != None :#checking out parent is greater then child or not 
            if w.parent.Left == u :
                w.parent.Left = w
            else:
                w.parent.Right = w
        u.Left = w.Right
        if u.Left != None :
            u.Left.parent = u
            u.parent = w
            w.Right = u
        if u == self.root :
            self.root = w
            self.root.parent = None

    def add(self,x):# to add child in random binary search tree
        u = self.Insert(x)
        if u:
            self.bubble_up(u)
            return True
        return False 

    def bubble_up(self,u):# for sorting in it while adding
        while u != self.root and u.parent.p > u.p :#We create a new node, u
            if u.parent.Right == u :
                self.rotate_left(u.parent)
            else:

                self.rotate_right(u.parent)
        if u.parent == None:
            self.root = u
#The remove in a Treap is the opposite of the add operation
    def remove(self,x):# removing child from RBST
        u = self.FindMin()
        t = self.FindMax()
        if u != None and u.value == x or t.value == x:#search for the node, u, containing x, then perform rotations to move u downwards until it becomes a leaf
            self.trickle_down(u)
            self.Delete(x)
            return True
        return False

    def trickle_down(self,u):
        while u.Left != None or u.Right != None:
            if u.Left == None:
                self.rotate_left(u.parent)
            elif u.Right == None:
                self.rotate_right(u.parent)
            elif u.Left.p < u.Right.p:
                self.rotate_right(u.parent)
            else:
                self.rotate_left(u.parent)
            if self.root == u:
                self.root = u.parent

obj = Random_BST()
# Creating new Nodes
obj.add(5)
obj.add(4)
obj.add(9)
obj.add(7)
# Removing Nodes
obj.remove(9)
obj.remove(4)




