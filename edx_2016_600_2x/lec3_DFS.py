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

def DFS(graph, start, end, path=[], shortest=None):
    """Depth First Search
    ===
    going deeper and deeper, until it either reaches the goal node
    or a node with no children
    ===
    graph: default is di-graph
    start: node
    end: node
    path: used to keep track of where we are in our exploration of the graph
    shortest: used to keep track of the best solution found so far
    """
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    # first add start node to the explored path
    path = path + [start]

    print("trying from Start[{}] to End[{}]".format(start, end))
    print("$$$ Current Shortest is: ", shortest, " $$$")
    print("Start is: ", start)
    print("End is: ", end)
    print("Build upon DFS path: [", printPath(path), " ]")

    # Base Case when start is end, return explored path
    if start == end:
        # start is end, path=[start]
        print("*** Reached Destination ***")
        print("*** returned path: {} ***".format(printPath(path)))
        return path

    print("Children of Start: ")
    for node in graph.childrenOf(start):
        if node not in path: # avoid cycles
            print("    ", node, " for Start ", start)
            # shortest default is None
            """rather than checking all of the paths at the end of the algorithm,
            we keep track of the shortest path from start to end found so far"""
            if shortest == None:
                print("shortest == None, proceed to try...")
                newPath = DFS(graph, node, end, path, shortest)
                # if there is a path from start to end
                if newPath != None:
                    print("FOUND A NEW Valid PATH")
                    shortest = newPath
                else:
                    print("No path found")
            elif len(path) < len(shortest):
                print("explored path is shorter than the current shortest, try it!")
                newPath = DFS(graph, node, end, path, shortest)
                # if there is a path from start to end
                if newPath != None:
                    print("FOUND A NEW SHORTER PATH")
                    shortest = newPath
                else:
                    print("No path found")
        else:
            print("    ", node, " for Start ", start)
            print('Already visited', node)
    # end of for loop of childrenOf(start)

    return shortest # usually return None unless newPath != None

solutions = []

def build_DFS_list(graph, start, end, path=[]):
    """instead of Depth First Search,
    return a list of all the path from start to end
    ===
    going deeper and deeper, until it either reaches the goal node
    or a node with no children
    ===
    graph: default is di-graph
    start: node
    end: node
    path: used to keep track of where we are in our exploration of the graph
    solutions: used to keep track of all the solutions found so far
    """
    path = path + [start]
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("trying from Start[{}] to End[{}]".format(start, end))
    print("Start is: ", start)
    print("End is: ", end)

    print("Explored DFS path: [", printPath(path), " ]")

    # Base Case when start is end, return explored path
    if start == end:
        # start is end, path=[start]
        print("*** Reached Destination ***")
        return path

    print("Children of Start: ")
    for node in graph.childrenOf(start):
        print("    ", node, " for Start ", start)
        if node not in path: # avoid cycles
            print(str(node) + " not in path")
            newPath = build_DFS_list(
                graph, node, end, path
            )
            print("returned newPath is: ", printPath(newPath))
            # if there is a path from start to end
            if newPath != None:
                global solutions
                solutions.append(newPath)
        else:
            print('Already visited', node)
    # end of for loop of childrenOf(start)

    return newPath

def get_DFS_list(source, destination):
    cityGraph = buildCityGraph(Digraph)
    return build_DFS_list(cityGraph, cityGraph.getNode(source), cityGraph.getNode(destination))

def get_DFS_path(source, destination):
    cityGraph = buildCityGraph(Digraph)
    return DFS(cityGraph,
               cityGraph.getNode(source),
               cityGraph.getNode(destination)
            )