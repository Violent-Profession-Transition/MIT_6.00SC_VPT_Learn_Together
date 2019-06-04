import string
from graph import Digraph, Edge, Node, \
                  WeightedEdge, WeightedDigraph, \
                   v2_WeightedDigraph
# import the helper functions for Prob3 and 4
from utils import *


# test for problem 1
# see the graph implementation
normal_g = Digraph()
weighted_g = WeightedDigraph()  # with self.edges as complex tuple
v2_weighted_g = v2_WeightedDigraph()  # with self.weights

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

for node in [A,B,C,D]:
    normal_g.addNode(node)
    weighted_g.addNode(node)
    v2_weighted_g.addNode(node)

# for normal digraph
normal_g.addEdge(Edge(A, B))
normal_g.addEdge(Edge(A, C))
normal_g.addEdge(Edge(B, C))
normal_g.addEdge(Edge(C, A))
normal_g.addEdge(Edge(C, D))

# for two versions of weightedDigrap
weighted_g.addEdge(WeightedEdge(A, B, 4, 2))
weighted_g.addEdge(WeightedEdge(A, C, 5, 2))
weighted_g.addEdge(WeightedEdge(B, C, 3, 1))
weighted_g.addEdge(WeightedEdge(C, A, 5, 2))
weighted_g.addEdge(WeightedEdge(C, D, 7, 6))

v2_weighted_g.addEdge(WeightedEdge(A, B, 4, 2))
v2_weighted_g.addEdge(WeightedEdge(A, C, 5, 2))
v2_weighted_g.addEdge(WeightedEdge(B, C, 3, 1))
v2_weighted_g.addEdge(WeightedEdge(C, A, 5, 2))
v2_weighted_g.addEdge(WeightedEdge(C, D, 7, 6))

#print WeightedEdge(C, D,7,6)
"""
# print the graphs to test
print "=====normal digraph: \n", normal_g
print "C's children: \n", normal_g.childrenOf(C)
print "getNode D: \n", normal_g.getNode("D")
print "nodes: \n", normal_g.nodes #set([C, D, A, B])
print "edges: \n", normal_g.edges #{C: [A, D], D: [], A: [B, C], B: [C]}

print "~~~~~weighted digraph: \n", weighted_g
print "nodes: \n", weighted_g.nodes #set([C, D, A, B])
print "edges: \n", weighted_g.edges #{C: [(A, 5, 2), (D, 7, 6)], D: [], A: [(B, 4, 2), (C, 5, 2)], B: [(C, 3, 1)]}


print ">>>>>weighted digraph with self.weights: ", v2_weighted_g
print "nodes: \n", v2_weighted_g.nodes #set([C, D, A, B])
print "edges: \n", v2_weighted_g.edges #{C: [A, D], D: [], A: [B, C], B: [C]}
print "weights: \n", v2_weighted_g.weights #{('B', 'C'): (3, 1), ('C', 'A'): (5, 2), ('A', 'B'): (4, 2), ('C', 'D'): (7, 6), ('A', 'C'): (5, 2)}
"""

#
# Problem 2: Building up the Campus Map
# Pseudo-Code:
# 1 for each line of map txt file
# 2 add 0th and 1st column as Nodes
# 3 try catch the duplicate valueError while adding nodes
# 3 addWeightedEdge(0th, 1st col, 2nd, 3rd col)

def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # print "Loading map from file..."
    # initilize a weighted digraph
    # w_g = WeightedDigraph()
    w_g = v2_WeightedDigraph()
    # read the map.txt file
    dataFile = open(mapFilename, 'r')
    for line in dataFile:
        dataLine = string.split(line) # split by space
        # print "dataLine is now: ", dataLine
        # dataLine is ['14', '50', '25', '20']
        # try getting the node instead of creating one
        if type(w_g.getNode(dataLine[0])) == Node:
            src = w_g.getNode(dataLine[0])
        else:
            src = Node(dataLine[0])
            w_g.addNode(src)
            # print "added ", dataLine[0]
        if type(w_g.getNode(dataLine[1])) == Node:
            dest = w_g.getNode(dataLine[1])
        else:
            dest = Node(dataLine[1])
            w_g.addNode(dest)
            # print "added ", dataLine[1]
        # create a weightedEdge
        tot_dist = float(dataLine[2])
        outdoor_dist = float(dataLine[3])
        w_edge = WeightedEdge(src, dest, tot_dist, outdoor_dist)
        w_g.addEdge(w_edge)
        #print "added weighted Edge: ", w_edge
    #print "now weightedGraph is: ", w_g
    dataFile.close()
    return w_g


#build a graph
mit_graph = load_map("mit_map.txt")

# print mit_graph.edges
# print mit_graph.weights
"""
n1 = mit_graph.getNode("32")
n2 = mit_graph.getNode("56")
n3 = mit_graph.getNode("66")
print n1
print n2
print n3
print mit_graph.childrenOf(n1)
# -> children of 32 is: [36, 57, 76, 68, 16, 12, 46, 48, 66, 56]
"""

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
#

# test for cal_dists()
# print cal_dists(v2_weighted_g, [A, B, C, D])
# -> (14,9)

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    shortestPath = None
    shortest_dist = maxTotalDist
    # print "digraph input is: ", digraph
    # print digraph.weights
    # for the graph.weights
    # {('B', 'C'): (3, 1), ('C', 'A'): (5, 2), ('A', 'B'): (4, 2), ('C', 'D'): (7, 6), ('A', 'C'): (5, 2)}
    all_paths = DFS_all(digraph, digraph.getNode(start), digraph.getNode(end))
    print "all_paths: ", all_paths
    for p in all_paths:
        print "trying path: ", p
        curr_totDist, curr_outDist = cal_dists(digraph, p)
        print "Dists: ", curr_totDist, curr_outDist
        if curr_totDist < shortest_dist and curr_outDist <= maxDistOutdoors:
            print "found a new VALID shortestPath"
            shortest_dist = curr_totDist
            shortestPath = p
    if shortestPath == None:
        raise ValueError("Exists no path that satisfies maxTotalDist and maxDistOutdoors constraints")
    # convert the shortestPath to list of str
    return [e.getName() for e in shortestPath]


# test Problem 3

#print v2_weighted_g
# DFS() from lectures
# print(DFS_all(v2_weighted_g, v2_weighted_g.getNode("A"), v2_weighted_g.getNode("D")))
# -> [[A, B, C, D], [A, C, D]]

# print DFS_all(mit_graph, mit_graph.getNode("57"), mit_graph.getNode("32"))
# -> [[57, 32]]
# print DFS_all(mit_graph, mit_graph.getNode("1"), mit_graph.getNode("7"))

# print bruteForceSearch(v2_weighted_g, "A", "D", 1000, 1000)
# print bruteForceSearch(mit_graph, '32', '56', 1000, 1000)


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    startNode = digraph.getNode(start)
    endNode = digraph.getNode(end)
    shortestPath = DFS_with_weight_lite(digraph, startNode, endNode, maxDistOutdoors)
    #print "AHAHH", cal_dists(digraph, shortestPath)
    if shortestPath == None or cal_dists(digraph, shortestPath)[0] >= maxTotalDist:
        raise ValueError("Exists no path that satisfies maxTotalDist and maxDistOutdoors constraints")
    # convert the shortestPath to list of str
    return [e.getName() for e in shortestPath]

# shortestPath test
# print DFS_with_weight_lite(v2_weighted_g, v2_weighted_g.getNode("A"), v2_weighted_g.getNode("D"), 100)
# print DFS_with_weight(mit_graph, mit_graph.getNode("57"), mit_graph.getNode("32"), 100)
# -> [57, 32]
# print DFS_with_weight(mit_graph, mit_graph.getNode("1"), mit_graph.getNode("7"), 100)
# -> [1, 5, 7]

# print DFS_with_weight(mit_graph, mit_graph.getNode("1"), mit_graph.getNode("32"), 100000)
# -> Expected:  ['1', '4', '12', '32'] (236.0, 145.0)

#assert False
#Uncomment below when ready to test
if __name__ == '__main__':
  # Test cases
  digraph = load_map("mit_map.txt")

  LARGE_DIST = 1000000

  # Test case 1
  print "---------------"
  print "Test case 1:"
  print "Find the shortest-path from Building 32 to 56"
  expectedPath1 = ['32', '56']
  #brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
  dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
  print "Expected: ", expectedPath1, cal_dists(digraph, expectedPath1)
  #print "Brute-force: ", brutePath1
  print "DFS: ", dfsPath1, cal_dists(digraph, dfsPath1)

  # Test case 2
  print "---------------"
  print "Test case 2:"
  print "Find the shortest-path from Building 32 to 56 without going outdoors"
  expectedPath2 = ['32', '36', '26', '16', '56']
  #brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
  dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
  print "Expected: ", expectedPath2, cal_dists(digraph, expectedPath2)
  #print "Brute-force: ", brutePath2
  print "DFS: ", dfsPath2, cal_dists(digraph, dfsPath2)

  # Test case 3
  print "---------------"
  print "Test case 3:"
  print "Find the shortest-path from Building 2 to 9"
  expectedPath3 = ['2', '3', '7', '9']
  #brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
  dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
  print "Expected: ", expectedPath3, cal_dists(digraph, expectedPath3)
  #print "Brute-force: ", brutePath3
  print "DFS: ", dfsPath3, cal_dists(digraph, dfsPath3)

  # Test case 4
  print "---------------"
  print "Test case 4:"
  print "Find the shortest-path from Building 2 to 9 without going outdoors"
  expectedPath4 = ['2', '4', '10', '13', '9']
  #brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
  dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
  print "Expected: ", expectedPath4, cal_dists(digraph, expectedPath4)
  #print "Brute-force: ", brutePath4
  print "DFS: ", dfsPath4, cal_dists(digraph, dfsPath4)

  # Test case 5
  print "---------------"
  print "Test case 5:"
  print "Find the shortest-path from Building 1 to 32"
  expectedPath5 = ['1', '4', '12', '32']
  #brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
  dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
  print "Expected: ", expectedPath5, cal_dists(digraph, expectedPath5)
  #print "Brute-force: ", brutePath5
  print "DFS: ", dfsPath5, cal_dists(digraph, dfsPath5)

  # Test case 6
  print "---------------"
  print "Test case 6:"
  print "Find the shortest-path from Building 1 to 32 without going outdoors"
  expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
  #brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
  dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
  print "Expected: ", expectedPath6, cal_dists(digraph, expectedPath6)
  #print "Brute-force: ", brutePath6
  print "DFS: ", dfsPath6, cal_dists(digraph, dfsPath6)

  # Test case 7
  print "---------------"
  print "Test case 7:"
  print "Find the shortest-path from Building 8 to 50 without going outdoors"
  #bruteRaisedErr = 'No'
  dfsRaisedErr = 'No'
  #try:
  #    bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
  #except ValueError:
  #    bruteRaisedErr = 'Yes'

  try:
      directedDFS(digraph, '8', '50', LARGE_DIST, 0)
  except ValueError:
      dfsRaisedErr = 'Yes'

  print "Expected: No such path! Should throw a value error."
  #print "Did brute force search raise an error?", bruteRaisedErr
  print "Did DFS search raise an error?", dfsRaisedErr

  # Test case 8
  print "---------------"
  print "Test case 8:"
  print "Find the shortest-path from Building 10 to 32 without walking"
  print "more than 100 meters in total"
  #bruteRaisedErr = 'No'
  dfsRaisedErr = 'No'
  #try:
  #    bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
  #except ValueError:
  #    bruteRaisedErr = 'Yes'

  try:
      directedDFS(digraph, '10', '32', 100, LARGE_DIST)
  except ValueError:
      dfsRaisedErr = 'Yes'

  print "Expected: No such path! Should throw a value error."
  #print "Did brute force search raise an error?", bruteRaisedErr
  print "Did DFS search raise an error?", dfsRaisedErr
