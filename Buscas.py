import networkx as nx
import collections
class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def putright(self, x):
        self.elements.append(x)

    def putleft(self, x):
        self.elements.appendleft(x)
    
    def get(self):
        return self.elements.popleft()

    def pop(self):
        return self.elements.pop()

    def remove(self,x):
        return self.elements.remove(x)

class Stack:
    def __init__(self):
        self.elements = collections.deque()
    
    def push(self,x):
        self.elements.append(x)

    def pop(self):
        return self.elements.pop()

    def get(self):
        aux = self.elements.pop()
        self.elements.append(aux)
        return aux

    def empty(self):
        return len(self.elements) == 0

g = nx.Graph()

g.add_nodes_from(['a','b','c','d','e','f','g'])

g.to_directed()


g.add_edge('b', 'e', weight = 4)
g.add_edge('b', 'd', weight = 4)
g.add_edge('a', 'b', weight = 2)  


g.add_edge('c', 'f', weight = 2)
g.add_edge('a', 'c', weight = 3)


g.add_edge('e', 'g', weight = 4)
g.add_edge('a', 'e', weight = 8)


g.add_edge('f', 'g', weight = 4)

def BFS(graph,start,final):
    frontier = Queue()
    frontier.putright(start)
    visited = {}
    visited[start] = True
    easyway = Queue()
    while not frontier.empty():
        aux = frontier.get()
        frontier.putleft(aux)
        if not aux == final:
            current =  frontier.get()
            frontiercur = Queue()
            neighbors = graph[current]
            visited[current]=True
            if not len(neighbors) == 1:
                easyway.putright(current)
            for i in neighbors:
                if not i in visited:
                    if not frontiercur.empty():
                        aux = frontiercur.get()
                        frontiercur.putleft(aux)
                    if frontiercur.empty():
                        frontiercur.putright(i)
                    elif graph.get_edge_data(i,current) <= graph.get_edge_data(aux,current):
                        frontiercur.putleft(i)
                    else:
                        frontiercur.putright(i)

            while True:
                try:
                    aux = frontiercur.pop()
                    if aux in frontier.elements:
                        frontier.remove(aux)
                    frontier.putleft(aux)
                except IndexError:
                    break
        else:
            easyway.putright(aux)
            print easyway.elements
            break
    return easyway.elements

def DFS(graph,start,final,visited):
    DFSpath = Queue()
    DFS_fun(graph,start,final,visited,DFSpath)
    DFSpath.putleft(start)
    print DFSpath.elements
    return DFSpath.elements


def DFS_fun(graph,start,final,visited,path):
    frontier = Stack()
    frontier.push(start)
    visited[start] = True
    end = False
    while not frontier.empty():
        current =  frontier.get()
        if not current == final:
            neighbors = graph[current]
            visited[current]=True
            for i in neighbors:
                if not i in visited:
                    if DFS_fun(graph,i,final,visited,path):
                        path.putleft(i)
                        return True
            frontier.pop()
        else:
            frontier.pop()
            end = True   
    return end

def BiDirS(graph,start,final):
    return

def BCU(graph,start,final):
    nonvisited = Queue()
    dist = {}
    prev = {}
    for v in graph:             
        dist[v] = 1000000001                 
        prev[v] = "0"
        nonvisited.putright(v)                          

    dist[start] = 0                        
    u = 0
    v = 1000000001

    while not nonvisited.empty(): 
        for i in nonvisited.elements:
            aux = graph.get_edge_data(i,start)
            if aux == None:
                aux = {}
                aux['weight'] =  1000000001
            if aux['weight'] < v:
                v = aux['weight']
                u = i

        print nonvisited.elements
        nonvisited.remove(u)


        for v in graph[u]:         
            weight = graph.get_edge_data(u, start)
            if weight != None:
                alt = weight['weight'] + graph.get_edge_data(u, v)['weight']
            else:
                alt = graph.get_edge_data(u, v)['weight']
            if alt < dist[v]:              
                dist[v] = alt 
                prev[v] = u 

    path = Stack()
    u = final
    while prev[u] != "0":
        path.push(u)
        u =  prev[u]
    path.push(start)

    print path.elements
    return path.elements


start_state = raw_input("Start: ")
final_state = raw_input("Final: ")

print "BFS :"
BFS(g,start_state,final_state)

print "DFS : "
DFS(g,start_state,final_state,{})

print "BiDirS : "
BiDirS(g,start_state,final_state) 

print "BCU : "
BCU(g,start_state,final_state)