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
    print "Loading map from file..."
    # initilize a weighted digraph
    w_g = WeightedDigraph()
    # read the map.txt file
    dataFile = open(mapFilename, 'r')
    for line in dataFile:
        dataLine = string.split(line) # split by space
        src = Node(dataLine[0])
        dest = Node(dataLine[1])
        tot_dist = dataLine[2]
        outdoor_dist = dataLine[3]
        #print "dataLine is now: ", dataLine
        # dataLine is ['14', '50', '25', '20']
        try:
            w_g.addNode(src)
            #print "added ", dataLine[0]
        except ValueError:
            pass
        try:
            w_g.addNode(dest)
            #print "added ", dataLine[1]
        except ValueError:
            pass
        # create a weightedEdge
        w_edge = WeightedEdge(src, dest, tot_dist, outdoor_dist)
        w_g.addEdge(w_edge)
        #print "added weighted Edge: ", w_edge
    #print "now weightedGraph is: ", w_g
    dataFile.close()
    return w_g


# test for load_map()
#load_map("mit_map.txt")

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
#

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
    #TODO
    pass

# test Problem 3
#build a graph
mit_graph = load_map("mit_map.txt")

#print test_graph
#print AllValidPath(test_graph, A, C, toPrint = False, visited = [])
#print all_valid_path
#build_DFS_list(test_graph, A, C)
#print solutions
#print mit_graph



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
    #TODO
    pass

"""
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
  brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
  dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
  print "Expected: ", expectedPath1
  print "Brute-force: ", brutePath1
  print "DFS: ", dfsPath1

  # Test case 2
  print "---------------"
  print "Test case 2:"
  print "Find the shortest-path from Building 32 to 56 without going outdoors"
  expectedPath2 = ['32', '36', '26', '16', '56']
  brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
  dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
  print "Expected: ", expectedPath2
  print "Brute-force: ", brutePath2
  print "DFS: ", dfsPath2

  # Test case 3
  print "---------------"
  print "Test case 3:"
  print "Find the shortest-path from Building 2 to 9"
  expectedPath3 = ['2', '3', '7', '9']
  brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
  dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
  print "Expected: ", expectedPath3
  print "Brute-force: ", brutePath3
  print "DFS: ", dfsPath3

  # Test case 4
  print "---------------"
  print "Test case 4:"
  print "Find the shortest-path from Building 2 to 9 without going outdoors"
  expectedPath4 = ['2', '4', '10', '13', '9']
  brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
  dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
  print "Expected: ", expectedPath4
  print "Brute-force: ", brutePath4
  print "DFS: ", dfsPath4

  # Test case 5
  print "---------------"
  print "Test case 5:"
  print "Find the shortest-path from Building 1 to 32"
  expectedPath5 = ['1', '4', '12', '32']
  brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
  dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
  print "Expected: ", expectedPath5
  print "Brute-force: ", brutePath5
  print "DFS: ", dfsPath5

  # Test case 6
  print "---------------"
  print "Test case 6:"
  print "Find the shortest-path from Building 1 to 32 without going outdoors"
  expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
  brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
  dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
  print "Expected: ", expectedPath6
  print "Brute-force: ", brutePath6
  print "DFS: ", dfsPath6

  # Test case 7
  print "---------------"
  print "Test case 7:"
  print "Find the shortest-path from Building 8 to 50 without going outdoors"
  bruteRaisedErr = 'No'
  dfsRaisedErr = 'No'
  try:
      bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
  except ValueError:
      bruteRaisedErr = 'Yes'

  try:
      directedDFS(digraph, '8', '50', LARGE_DIST, 0)
  except ValueError:
      dfsRaisedErr = 'Yes'

  print "Expected: No such path! Should throw a value error."
  print "Did brute force search raise an error?", bruteRaisedErr
  print "Did DFS search raise an error?", dfsRaisedErr

  # Test case 8
  print "---------------"
  print "Test case 8:"
  print "Find the shortest-path from Building 10 to 32 without walking"
  print "more than 100 meters in total"
  bruteRaisedErr = 'No'
  dfsRaisedErr = 'No'
  try:
      bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
  except ValueError:
      bruteRaisedErr = 'Yes'

  try:
      directedDFS(digraph, '10', '32', 100, LARGE_DIST)
  except ValueError:
      dfsRaisedErr = 'Yes'

  print "Expected: No such path! Should throw a value error."
  print "Did brute force search raise an error?", bruteRaisedErr
  print "Did DFS search raise an error?", dfsRaisedErr
"""