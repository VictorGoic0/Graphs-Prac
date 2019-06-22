class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def remove_from_head(self):
    current_head = self.head
    self.delete(self.head)
    self.head = current_head.next
    return current_head.value

  def add_to_tail(self, value):
    if self.tail:
      current_tail = self.tail
      self.tail.insert_after(value)
      self.tail = ListNode(value, current_tail)
      current_tail.next = self.tail
    else:
      self.tail = ListNode(value)
      self.head = self.tail
    self.length += 1

  def remove_from_tail(self):
    current_tail = self.tail
    self.delete(self.tail)
    self.tail = current_tail.prev
    return current_tail.value

  def delete(self, node):
    if node.prev == None:
      self.head = node.next
    elif node.next == None:
      self.tail = node.prev
    node.delete()
    self.length -= 1
    if (self.length == 0):
      self.head = None
      self.tail = None

class Queue:
  def __init__(self):
    self.length = 0
    self.storage = DoublyLinkedList()
  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.length += 1
  def dequeue(self):
    if self.length == 0:
      return None
    else:
      item = self.storage.remove_from_head()
      self.length -= 1
      return item
  def size(self):
    return self.length

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

