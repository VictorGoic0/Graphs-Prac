import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        if numUsers <= avgFriendships:
            return "The number of users must be greater than the average number of friendships."

        self.lastID = 0
        self.users = {}
        self.friendships = {}

        for i in range(numUsers):
            self.addUser(f'randomUser#{i+1}')

        for userID, user in self.users.items():
            numOfFriends = random.randint(0, avgFriendships)
            for i in range(numOfFriends):
                randomFriendID = random.randint(1, numUsers)
                if randomFriendID != userID and randomFriendID not in self.friendships[userID]:
                    self.addFriendship(userID, randomFriendID)

    def getAllSocialPaths(self, userID):
        if userID not in self.friendships:
            return -1

        if len(self.friendships[userID]) == 0:
            return {}

        def bfs(graph, starting_vertex):
            q = Queue()
            q.enqueue([starting_vertex])
            friendships = {}
            while q.size() > 0:
                path = q.dequeue()
                vertex = path[-1]
                if vertex not in friendships:
                    friendships[vertex] = path
                    for friend in graph[vertex]:
                        if friend not in friendships:
                            new_path = path[:]
                            new_path.append(friend)
                            q.enqueue(new_path)
            return friendships
        socialPaths = bfs(self.friendships, userID)
        return socialPaths
        

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(100000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)