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

def earliest_ancestor(ancestors, person):
    graph = {}
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = set()
            graph[child].add(parent)
    if person not in graph:
        return -1
    else:
        def dfs(graph, starting_vertex):
            stack = Stack()
            stack.push([starting_vertex])
            visited = set()
            paths = {}
            maxLength = 0
            while stack.size() > 0:
                path = stack.pop()
                node = path[-1]
                if node not in visited and node in graph:
                    visited.add(node)
                    for parent in graph[node]:
                        new_path = path[:]
                        new_path.append(parent)
                        stack.push(new_path)
                elif node not in graph:
                    length = len(path)
                    if length > maxLength:
                        maxLength = length
                    if length not in paths:
                        paths[length] = [path]
                    else:
                        paths[length].append(path)
            if len(paths[maxLength]) == 1:
                return paths[maxLength][0][-1]
            else:
                minimum = []
                for subArray in paths[maxLength]:
                    minimum.append(subArray[-1])
                return min(minimum)
        ancestor = dfs(graph, person)
        return ancestor