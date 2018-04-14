class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

class UnOrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                print "Item Found -> %d" % item
                break
            else:
                current = current.next

    def count(self):
        counter = 0
        current = self.head
        while current != None:
            counter = counter + 1
            current = current.next

        print "Total Item In List -> %d" % counter

    def print_item(self):
        current = self.head
        while current != None:
            print current.data
            current = current.next

    def delete(self, item):
        current = self.head
        while current != None:
            if current.data == item:



myList = UnOrderedList()
myList.add(10)
myList.add(15)
myList.print_item()
myList.search(15)
myList.count()
