from collections import deque
class Node(object):
    def __init__(self,key=None,data=None):
        self.sortkey = key
        self.left = None
        self.right = None
        self.data=data

class BST(object):
    def __init__(self):
        self.first=None
        self.lenght=0

    #adds a node to the Binary search tree            
    def Insert(self,key,data=None):
        if self.first ==None:
            self.first=Node(key,data)
        else:
            self._insertNode(self.first,key,data)
                
    def _insertNode(self,current,key,data=None):
            if current.sortkey > key:
                if current.left == None :
                    current.left = Node(key,data)
                else:
                    self._insertNode(current.left,key,data)
            else:
                if current.right == None :
                    current.right = Node(key,data)
                else:
                    self._insertNode(current.right,key,data)

    #Remove first node which matches sortkey         
    def Remove(self,key):
        if self.first == None:
            #test for empty tree
            return False
        to_remove = self._RecursiveSearch(self.first,key)
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
        return self._RecursiveFindParent(self.first,node.sortkey)

    def _RecursiveFindParent(self,current,key):
        if current.sortkey == key:
            #First Node
            return None
        elif key < current.sortkey:
            if key==current.left.sortkey:
                return current
            else:
                return self._RecursiveFindParent(current.left,key)
        else:
            if key==current.right.sortkey:
                return current
            else:
                return self._RecursiveFindParent(current.right,key)

    def FindMax(self,root):
        while root.right != None:
            root=root.right
        return root
 
    def FindMin(self,root):
        while root.left != None:
            root=root.left
        return root

    def Search(self,key):
        current = self.first
        if current == None:
            return None
        return self._RecursiveSearch(self.first,key)

    def _RecursiveSearch(self,current,key):
        if current.sortkey == key:
            return current
        elif key < current.sortkey:
            return self._RecursiveSearch(current.left,key)
        else:
            return self._RecursiveSearch(current.right,key)

   # prints the Binary tree structure to the console   
    def __repr__(self):
        result=''
        q=deque()
        if self.first==None:
            return "Empty"
        else:
            result+= str(self.first.sortkey)+" "
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
                    if current.sortkey<old.sortkey:
                        result+="\n"
                    result+=str(current.sortkey)+" "
                else:
                    current=None
        return result