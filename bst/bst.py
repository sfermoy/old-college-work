from collections import deque
class Node(object):
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.first=None
        self.lenght=0
   #adds a node to the Binary search tree            
    def Insert(self,val):
        if self.first ==None:
            self.first=Node(val)
        else:
            self._insertNode(self.first,val)
                
    def _insertNode(self,current,val):
            if current.value > val:
                if current.left == None :
                    current.left = Node(val)
                else:
                    self._insertNode(current.left,val)
            else:
                if current.right == None :
                    current.right = Node(val)
                else:
                    self._insertNode(current.right,val)

    #Remove first node which matches value         
    def Remove(self,value):
        return value
    
    def BreadthFirst(self):
        return False

   # prints the Binary tree structure to the console   
    def __repr__(self):
        result=''
        q=deque()
        if self.first==None:
            pass
        else:
            result+= str(self.first.value)+" "
            current=self.first
            count=0
            while current != None:
                
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
        
    def __str__(self):
        result=''
        
        return result
