#<------------------------------------------1---------------------------------------------->
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, index, x):
        if index < 0:
            return None
        node = Node(x)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    return None
                current = current.next
            node.next = current.next
            current.next = node
        return node

    def insertAtHead(self, x):
        return self.insertNode(0, x)

    def insertAtEnd(self, x):
        current = self.head
        if current is None:
            self.head = Node(x)
        else:
            while current.next is not None:
                current = current.next
            current.next = Node(x)

    def findNode(self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                return True
            current = current.next
        return False

    def deleteNode(self, x):
        current = self.head
        previous = None
        while current is not None:
            if current.data == x:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next

    def deleteFromStart(self):
        if self.head is not None:
            self.head = self.head.next

    def deleteFromEnd(self):
        current = self.head
        previous = None
        while current is not None:
            if current.next is None:
                if previous is None:
                    self.head = None
                else:
                    previous.next = None
                return
            previous = current
            current = current.next

    def displayList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverseList(self):
        current = self.head
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
        return self

    def sortList(self, list):
        if list is None or list.next is None:
            return list
        middle = self.getMiddle(list)
        next_to_middle = middle.next
        middle.next = None
        left = self.sortList(list)
        right = self.sortList(next_to_middle)
        return self.mergeLists(left, right)

    def getMiddle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.data < list2.data:
            result = list1
            result.next = self.mergeLists(list1.next, list2)
        else:
            result = list2
            result.next = self.mergeLists(list1, list2.next)
        return result

    def removeDuplicates(self, list):
        if list is None:
            return list
        current = list
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return list

    def interestLists(self, list1, list2):
        result = LinkedList()
        current1 = list1.head
        while current1 is not None:
            if list2.findNode(current1.data):
                result.insertAtEnd(current1.data)
            current1 = current1.next
        return result
    
# Create the first linked list
list1 = LinkedList()
list1.insertAtEnd(1)
list1.insertAtEnd(2)
list1.insertAtEnd(3)
list1.insertAtEnd(4)

# Create the second linked list
list2 = LinkedList()
list2.insertAtEnd(3)
list2.insertAtEnd(4)
list2.insertAtEnd(5)
list2.insertAtEnd(6)

# Find the intersection of the two lists
result = LinkedList().interestLists(list1, list2)
result.displayList() 
    
#<------------------------------------------2---------------------------------------------->

# Implementation of a stack using arrays

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
# Create a new stack
s = Stack()

# Push some items
s.push(0)
s.push(14)
s.push(7)

# Pop an item
item = s.pop()
print(item)  # Output: 3

# Check if the stack is empty
print(s.is_empty())  # Output: False

# Get the size of the stack
print(s.size())  # Output: 2
    
#Implementation of a queue using arrays
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
# Create a new queue
q = Queue()

# Enqueue some items
q.enqueue(5)
q.enqueue(7)
q.enqueue(9)

# Dequeue an item
item = q.dequeue()
print(item)  # Output: 1

# Check if the queue is empty
print(q.is_empty())  # Output: False

# Get the size of the queue
print(q.size())  # Output: 2

#Implementation of a stack using linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return None
        item = self.head.data
        self.head = self.head.next
        return item

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
# Create a new stack
s = Stack()

# Push some items
s.push(10)
s.push(20)
s.push(30)

# Pop an item
item = s.pop()
print(item)  # Output: 3

# Check if the stack is empty
print(s.is_empty())  # Output: False

# Get the size of the stack
print(s.size())  # Output: 2

# Implementation of a queue using linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        node = Node(item)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None:
            return None
        item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return item

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
#Create a new queue
q = Queue()

# Enqueue some items
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Dequeue an item
item = q.dequeue()
print(item) 

# Check if the queue is empty
print(q.is_empty()) 

# Get the size of the queue
print(q.size())  

#<------------------------------------------3---------------------------------------------->

# Implementation of the Node class with prev pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Implementation of the DoublyLinkedList class

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insertNode(self, index, x):
        if index < 0:
            return None
        node = Node(x)
        if index == 0:
            node.next = self.head
            if self.head is not None:
                self.head.prev = node
            self.head = node
            if self.tail is None:
                self.tail = node
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    return None
                current = current.next
            node.next = current.next
            if current.next is not None:
                current.next.prev = node
            current.next = node
            node.prev = current
            if node.next is None:
                self.tail = node
        return node

    def insertAtHead(self, x):
        return self.insertNode(0, x)

    def insertAtEnd(self, x):
        return self.insertNode(self.size(), x)

    def findNode(self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                return True
            current = current.next
        return False

    def deleteNode(self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                if current.next is None:
                    self.tail = current.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def deleteFromStart(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

    def deleteFromEnd(self):
        if self.tail is not None:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None

    def displayList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverseList(self):
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev

    def sortList(self, list):
        if list is None or list.next is None:
            return list
        middle = self.getMiddle(list)
        next_to_middle = middle.next
        middle.next = None
        left = self.sortList(list)
        right = self.sortList(next_to_middle)
        return self.mergeLists(left, right)

    def getMiddle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeLists(self, list1, list2):
        result = DoublyLinkedList()
        current1 = list1.head
        current2 = list2.head
        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                result.insertAtEnd(current1.data)
                current1 = current1.next
            elif current1.data > current2.data:
                result.insertAtEnd(current2.data)
                current2 = current2.next
            else:
                result.insertAtEnd(current1.data)
                current1 = current1.next
                current2 = current2.next
        while current1 is not None:
            result.insertAtEnd(current1.data)
            current1 = current1.next
        while current2 is not None:
            result.insertAtEnd(current2.data)
            current2 = current2.next
        return result

    def removeDuplicates(self, list):
        current = list.head
        while current is not None:
            while current.next is not None and current.data == current.next.data:
                current.next = current.next.next
            current = current.next
        return list

    def interestLists(self, list1, list2):
        result = DoublyLinkedList()
        current1 = list1.head
        while current1 is not None:
            if list2.findNode(current1.data):
                result.insertAtEnd(current1.data)
            current1 = current1.next
        return result

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
# Create the linked list
list1 = DoublyLinkedList()
list1.insertAtEnd(1)
list1.insertAtEnd(3)
list1.insertAtEnd(5)
list1.insertAtEnd(7)

# Create another linked list
list2 = DoublyLinkedList()
list2.insertAtEnd(2)
list2.insertAtEnd(3)
list2.insertAtEnd(7)
list2.insertAtEnd(8)

# Merge the two lists
result = list1.mergeLists(list1.head, list2.head)
result.displayList()  # Output: 1 2 3 3 5 7 7 8

# Remove duplicates from the merged list
result = list1.removeDuplicates(result)
result.displayList()  # Output: 1 2 3 5 7 8

# Find the intersection of the two lists
result = list1.interestLists(list1, list2)
result.displayList()  # Output: 3 7