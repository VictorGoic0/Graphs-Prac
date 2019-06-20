import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)