from collections import deque
import pdb
class Node(object):
    def __init__(self,val=None,data=None):
        self.value = val
        self.left = None
        self.right = None
        self.data=data

class BST(object):
    def __init__(self):
        self.first=None
        self.lenght=0

    #adds a node to the Binary search tree            
    def Insert(self,val,data=None):
        if self.first ==None:
            self.first=Node(val,data)
        else:
            self._insertNode(self.first,val,data)
                
    def _insertNode(self,current,val,data=None):
            if current.value > val:
                if current.left == None :
                    current.left = Node(val,data)
                else:
                    self._insertNode(current.left,val,data)
            else:
                if current.right == None :
                    current.right = Node(val,data)
                else:
                    self._insertNode(current.right,val,data)

    #Remove first node which matches value         
    def Remove(self,val):
        if self.first == None:
            #test for empty tree
            return False
        to_remove = self._RecursiveSearch(self.first,val)
        parent = self._FindParent(to_remove)
        if to_remove.right==None and to_remove.left==None:
            # Case 1 the node is a leaf
            if to_remove is self.first:
                self.first=None
            else:
                if parent.left is to_remove:   
                    parent.left=None
                else:
                    parent.right=None
            return False
        elif to_remove.right !=None:
            #Case 2 the Node has a Right subtree
            #if val=="google":
                #pdb.set_trace()
            themin=self.FindMin(to_remove.right)
            theminparent=self._FindParent(themin)

            if theminparent.right is themin:
                theminparent.right=themin.right
            else:
                theminparent.left=themin.right

            themin.left=to_remove.left
            themin.right=to_remove.right
            
            if parent==None:
                self.first=themin
            elif parent.left is to_remove:   
                parent.left=themin
            elif parent.right is to_remove:
                parent.right=themin
            return True
        elif to_remove.right ==None and to_remove.left!=None:
            #Case 3 the Node ONLY has a left subtree
            themax=self.FindMax(to_remove.left)
            themaxparent=self._FindParent(themax)
            if themaxparent.left is themax:
                themaxparent.left= themax.left
            else:
                themaxparent.right=themax.left
            themax.left=to_remove.left
            themax.right=to_remove.right
            if parent==None:
                self.first=themax
            elif parent.left is to_remove:   
                parent.left=themax
            elif parent.right is to_remove:
                parent.right=themax
            return True
        
    def _FindParent(self,node): 
        current=self.first
        if current == None:
            return None
        return self._RecursiveFindParent(self.first,node.value)

    def _RecursiveFindParent(self,current,val):
        if current.value == val:
            #First Node
            return None
        elif val < current.value:
            if val==current.left.value:
                return current
            else:
                return self._RecursiveFindParent(current.left,val)
        else:
            if val==current.right.value:
                return current
            else:
                return self._RecursiveFindParent(current.right,val)

    def FindMax(self,root):
        while root.right != None:
            root=root.right
        return root
 
    def FindMin(self,root):
        while root.left != None:
            root=root.left
        return root

    def Search(self,val):
        current = self.first
        if current == None:
            return None
        return self._RecursiveSearch(self.first,val)

    def _RecursiveSearch(self,current,val):
        if current.value == val:
            return current
        elif val < current.value:
            return self._RecursiveSearch(current.left,val)
        else:
            return self._RecursiveSearch(current.right,val)

   # prints the Binary tree structure to the console   
    def __repr__(self):
        result=''
        q=deque()
        if self.first==None:
            return "Empty"
        else:
            result+= str(self.first.value)+" "
            current=self.first
            count=0
            while current != None:
                    #pdb.set_trace()
                if current.left != None:
                    q.append(current.left)
                if current.right != None:
                    q.append(current.right)
                if q:
                    old=current
                    current=q.popleft()
                    if current.value<old.value:
                        result+="\n"
                    result+=str(current.value)+" "
                else:
                    current=None
        return result