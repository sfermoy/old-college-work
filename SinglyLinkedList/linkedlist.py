class Node(object):

        def __init__(self,value):
            self.value= value
            self.next=None
        
class LinkedList(object):
   
   def __init__(self):
        self.head=None
        self.tail=None
                
   def addNode(self,value):
        n= Node(value)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
            
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
       
   def test(self):
        if self.head != None:
            print "val ", self.head.value
            n=self.head
            while n.next != None:
                print "val ",n.next.value
                n=n.next
            print "value of head ",self.head.value
            print "value of tail ",self.tail.value,"\n"
        else:
            print "Empty"
