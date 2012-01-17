import DoublyLinkedList
def test(n):
    while n.next != None:
        if n.prev==None and n.next ==None:
            print str(n.value)+"\n"
        elif n.prev==None:
            print str(n.value)+str(n.next.value)+"\n"
        elif n.next==None:
            print str(n.prev.value)+str(n.value)+"\n"
        else :
            print str(n.prev.value)+str(n.value)+str(n.next.value)+"\n"
        n=n.next

l=DoublyLinkedList.DoublyLinkedList()
l.addLast(1)
l.addLast(2)
l.addLast(3)
l.addLast(4)
l.addLast(5)
l.addLast(6)
n=l.head
print repr(l)
test(n)
l.remove(3)
test(n)
l.removeFirst()
test(n)
print repr(l)