# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#

class Node(object):
   def __init__(self, name):
       self.name = str(name)
   def getName(self):
       return self.name
   def __str__(self):
       return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)

class Edge(object):
   def __init__(self, src, dest):
       self.src = src
       self.dest = dest
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def __str__(self):
       return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, total_dist, outdoor_dist):
        Edge.__init__(self, src, dest)
        self.total_dist = total_dist
        self.outdoor_dist = outdoor_dist
    def getTotalDistance(self):
        return self.total_dist
    def getOutdoorDistance(self):
        return self.outdoor_dist
    def __str__(self):
       return str(self.src) + '->' + str(self.dest) +\
            '(' + str(self.total_dist) +\
             ',' + str(self.outdoor_dist) + ')'


class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]
    def getNode(self, name):
        """
        name is a str
        """
        for n in self.nodes:
            if n.getName() == name:
                return n


class WeightedDigraph(Digraph):
    """
    WeightedDigraph is Digraph with new addEdge method
    """
    def addEdge(self, edge):
        """
        overwrites addEdge method from Digraph
        adds a tuple (Node, tot, outdoor) to the edges[src] list
        """
        src = edge.getSource()
        dest = edge.getDestination()
        dest_with_w = (
            edge.getDestination(),
            edge.getTotalDistance(),
            edge.getOutdoorDistance())
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest_with_w)


class v2_WeightedDigraph(Digraph):
    """
    instead of breaking the addEdge method and self.edges,
    version 2 tries creating a new attribute self.weights
    """
    def __init__(self):
        """inherit the init with self.nodes and self.edges
        """
        Digraph.__init__(self)
        # also init a self.weights similar to self.edges
        self.weights = {}

    def addEdge(self, edge):
        """
        creates self.weights from edge total dist and outdoor dist
        """
        # addEdge to self.edges like in Digraph
        Digraph.addEdge(self, edge)
        # then create self.weights from edge
        src = edge.getSource()
        dest = edge.getDestination()
        total_dist = edge.getTotalDistance()
        outdoor_dist = edge.getOutdoorDistance()
        self.weights[(str(src), str(dest))] = (total_dist, outdoor_dist)
