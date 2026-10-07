class Node:
    def __init__(self, val:int=None, next:Node=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        #start at head
        item = self.head

        for i in range(index):
            if item == None:
                return -1

            item = item.next

        if item == None:
            return -1
        return item.val

    def insertHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val=val, next=temp)       

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val=val)
            return

        #get to end of list
        item = self.head
        while item.next != None:
            item = item.next

        item.next = Node(val=val)

    def remove(self, index: int) -> bool:
        #remove head if needed
        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            return False

        #get to ith node
        item = self.head

        for i in range(index):
            previous = item
            item = item.next

            if item == None:
                return False

        #set previous item to point at the item after
        previous.next = item.next
        return True        

    def getValues(self) -> List[int]:
        arr = []
        item = self.head

        while item:
            arr.append(item.val)
            item = item.next

        return arr
        
