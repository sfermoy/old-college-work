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
l.addLast("elephant")
l.addLast(4)
l.addLast("snail")
l.addLast(6)
n=l.head
print repr(l)
l.remove(4)
print repr(l)
l.removeFirst()
#test(n)
print repr(l)