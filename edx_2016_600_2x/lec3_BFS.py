class Node:
    def __init__(self, name):
        """assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge:
    def __init__(self, src, dest):
        """assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() +\
            "-->" +\
            self.dest.getName()

class Digraph:
    """edges is a dict mapping each node
    to a list of its children (from type Edge)
    """
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if type(node) == str:
            raise ValueError("node should be of type node")
        if node in self.edges:
            raise ValueError("Duplicate node")
        else:
            # add node of an empty list
            self.edges[node] = []
    def addEdge(self, edge):
        """input is type edge
        get the Source Node and Destination Node
        from the Edge parameter"""
        # extract the src and dest from type edge
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Source or Destination Nodes not in graph yet")
        self.edges[src].append(dest)
    def childrenOf(self, node):
        """return the children list of that node"""
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name + " not in the graph")
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result +\
                        src.getName() +\
                        "-->" +\
                        dest.getName() +\
                        "\n"
        return result[:-1] # omit final newline

class Graph(Digraph):
    """inherits from Digraph"""
    def addEdge(self, edge):
        """add edge to add TWO edges,
        one in each direction"""
        Digraph.addEdge(self, edge)
        # add an edge using type Edge
        rev = Edge(edge.getDestination(), edge.getSource())
        # edge points both ways
        Digraph.addEdge(self, rev)

def buildCityGraph(graphType):
    g = graphType()
    for city in ('Boston', 'Providence', 'NY', 'Chicago', 'Denver', 'Phoenix', 'LA'):
        g.addNode(Node(city))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('NY')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('NY')))
    g.addEdge(Edge(g.getNode('NY'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('NY')))
    g.addEdge(Edge(g.getNode('LA'), g.getNode('Boston')))
    return g

def printPath(path):
    """path is a list of nodes [A,B,C...]
    print Node --> Node --> ... in the order of the list
    """
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        # except the last node
        if i != len(path) - 1:
            result += "-->"
    return result

def BFS(graph, start, end):
    """Breadth First Search"""

    initPath = [start]
    pathQueue = [initPath] # list of list [ [start] ]
    # `pathQueue` is used to store all of the paths currently
    # being explored

    while len(pathQueue) != 0:
        # get and remove oldest element in pathQueue
        # each iteration starts by removing a path from the pathQueue,
        # and assign that path to tempPath
        tempPath = pathQueue.pop(0)

        print("Current BFS path: ", printPath(tempPath))

        lastNode = tempPath[-1]

        if lastNode == end:
            """if the last node in tempPath is end,
            tempPath is the shortest path and is returned
            """
            return tempPath # found the shortest path

        for nextNode in graph.childrenOf(lastNode):
            """
            Otherwise a set of new paths is created,
            each of which extends tempPath by adding
            one of its children,
            each of these new paths is then added to the queue
            """
            if nextNode not in tempPath: # avoid cycles
                newPath = tempPath + [nextNode]
                pathQueue.append(newPath)
    return None

def get_BFS_path(source, destination):
    cityGraph = buildCityGraph(Digraph)
    return BFS(cityGraph,
               cityGraph.getNode(source),
               cityGraph.getNode(destination)
            )