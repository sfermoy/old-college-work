class Node(object):

    def __init__(self,val):
        self.value= val
        self.next=None
        
class LinkedList(object):
   
    def __init__(self):
        self.head=None
        self.tail=None
   
   #adds a node to the tail/end of the linked-list            
    def addLast(self,val):
        n = Node(val)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
            
   # Remove first node which matches value         
    def remove(self,value):
        if self.head == None:
            return False
            
        if self.head.value==value:
            if self.head is self.tail:
                self.head=None
                self.tail=None
                return True
            else:
                self.head=self.head.next
                return True
                
        n=self.head
        while n.next != None:
            if n.next.value ==value:
                if n.next.next ==None:
                     n.next=None
                     self.tail=n
                     return True
                else:
                    n.next=n.next.next
                    return True
            n=n.next
        return False
    
    def removeFirst(self):
        if self.head == None:
            return False
        if self.head is self.tail
            self.head=None
            self.tail=None
            return True
        else
            self.head=self.head.next
            return True
   

   # prints the linked list structure to the console   
    def __repr__(self):
        result=''
        if self.head != None:
            result += 'val '+ str(self.head.value)+ '\n'
            n=self.head
            while n.next != None:
                result += 'val '+ str(n.next.value) + '\n'
                n=n.next
            result += 'value of head '+ str(self.head.value)+ '\n'
            result += 'value of tail '+ str(self.head.value) + '\n'
        else:
            result += 'Empty'
        return result