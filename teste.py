import collections

class SimpleGraph:
    def __init__(self):
        self.edges = {}
        self.nodes = []
    
    def neighbors(self, id):
        return self.edges[id]

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()


graph = SimpleGraph()
graph.edges['A'] = {'B': 2, 'C': 3, 'E': 8}
graph.edges['B'] = {'A': 2, 'E': 4, 'D': 4}
graph.edges['C'] = {'A': 3, 'F': 2}
graph.edges['D'] = {'B': 4}
graph.edges['E'] = {'A': 8, 'B': 4, 'G': 4}
graph.edges['F'] = {'C': 2, 'G': 4}
graph.edges['G'] = {'E': 4, 'F': 4}

start = 'A'
frontier = Queue()
frontier.put(start)
visited = {}
visited[start] = True
while not frontier.empty():
	current = frontier.get()
	print("current: %r" % current)
	for next in graph.neighbors(current):
		print next
		if next not in visited:
			frontier.put(next)
			visited[next] = True