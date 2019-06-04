import time

def cal_dists(digraph, path):
    """input is path: list of nodes,
    digraph.weights maps the edges to the weights
    return a tuple (totalDist, DistOutdoors)
    """
    totalDist = 0
    DistOutdoors = 0
    # path = [A, B, C, D]
    # digraph.weights = {('B', 'C'): (3, 1), ('C', 'A'): (5, 2), ('A', 'B'): (4, 2), ('C', 'D'): (7, 6), ('A', 'C'): (5, 2)}
    for i in range(len(path)-1):
        (edge_tot_dist, edge_out_dist) = digraph.weights[(str(path[i]), str(path[i+1]))]
        totalDist += edge_tot_dist
        DistOutdoors += edge_out_dist
    return (totalDist, DistOutdoors)


def DFS_all(graph, start, end, path=None, all_paths=None):
    """Depth First Search, return all valid paths
    ===
    going deeper and deeper, until it either reaches the goal node
    or a node with no children
    ===
    graph: default is di-graph
    start: node
    end: node
    path: used to keep track of where we are in our exploration of the graph
    all_paths: all solutions found so far
    """
    #time.sleep(0.5)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if all_paths == None:
        #Initialize for first invocation
        all_paths = []
    if path == None:
        #Initialize for first invocation
        path = []
    # first add start node to the explored path
    path = path + [start]

    print "trying from Start[{}] to End[{}]".format(start, end)
    print "$$$ All paths: ", all_paths, " $$$"
    print "Start is: ", start
    print "End is: ", end
    print "Build upon DFS path: [", path, " ]"

    # Base Case when start is end, return explored path
    if start == end:
        # start is end, path=[start]
        print "*** Reached Destination ***"
        print "*** returned path: {} ***".format(path)
        all_paths.append(path)
        return all_paths

    print("Children of Start: ")
    for node in graph.childrenOf(start):
        if node not in path: # avoid cycles
            print "    ", node, " for Start ", start
            all_paths = DFS_all(graph, node, end, path, all_paths)
        else:
            print "    ", node, " for Start ", start
            print 'Already visited', node
    # end of for loop of childrenOf(start)

    return all_paths

def DFS_with_weight_lite(graph, start, end, maxOutdoor, path=[], shortest=None):
    # first add start node to the explored path
    path = path + [start]

    # Base Case when start is end, return explored path
    if start == end:
        # start is end, path=[start]
        return path

    for node in graph.childrenOf(start):
        if node not in path: # avoid cycles
            # shortest default is None
            """rather than checking all of the paths at the end of the algorithm,
            we keep track of the shortest path from start to end found so far"""
            if shortest == None:
                newPath = DFS_with_weight_lite(graph, node, end, maxOutdoor, path, shortest)
                # if there is a path from start to end
                if newPath != None and cal_dists(graph, newPath)[1] <= maxOutdoor:
                    shortest = newPath
            elif cal_dists(graph, path)[0] < cal_dists(graph, shortest)[0] and\
                cal_dists(graph, path)[1] <= maxOutdoor:
                newPath = DFS_with_weight_lite(graph, node, end, maxOutdoor, path, shortest)
                # if there is a path from start to end
                if cal_dists(graph, newPath)[1] <= maxOutdoor \
                    and cal_dists(graph, newPath)[0] < cal_dists(graph, shortest)[0]:
                    shortest = newPath
    # end of for loop of childrenOf(start)
    return shortest # usually return None unless newPath != None


def DFS_with_weight(graph, start, end, maxOutdoor, path=[], shortest=None):
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
    #time.sleep(0.01)
    # first add start node to the explored path
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    # first add start node to the explored path
    path = path + [start]

    print "trying from Start[{}] to End[{}]".format(start, end)
    print "$$$ Current Shortest is: ", shortest, " $$$"
    print "Start is: ", start
    print "End is: ", end
    print "Build upon DFS path: [", path, " ]"

    # Base Case when start is end, return explored path
    if start == end:
        # start is end, path=[start]
        print "*** Reached Destination ***"
        print "*** returned path: {} ***".format(path)
        return path

    print("Children of Start: ")
    for node in graph.childrenOf(start):
        if node not in path: # avoid cycles
            print "    ", node, " for Start ", start
            # shortest default is None
            """rather than checking all of the paths at the end of the algorithm,
            we keep track of the shortest path from start to end found so far"""
            if shortest == None:
                print "shortest == None, proceed to try..."
                newPath = DFS_with_weight(graph, node, end, maxOutdoor, path, shortest)
                # if there is a path from start to end
                if newPath != None and cal_dists(graph, newPath)[1] < maxOutdoor:
                    print "FOUND A NEW Valid PATH"
                    shortest = newPath
                else:
                    print "No path found"
            elif cal_dists(graph, path)[0] < cal_dists(graph, shortest)[0] and\
                cal_dists(graph, path)[1] <= maxOutdoor:
                print "explored path is shorter than the current shortest, try it!"
                newPath = DFS_with_weight(graph, node, end, maxOutdoor, path, shortest)
                # if there is a path from start to end
                if cal_dists(graph, newPath)[1] <= maxOutdoor \
                    and cal_dists(graph, newPath)[0] < cal_dists(graph, shortest)[0]:
                    print "FOUND A NEW SHORTER PATH"
                    shortest = newPath
                else:
                    print "No path found"
        else:
            print "    ", node, " for Start ", start
            print 'Already visited', node
    # end of for loop of childrenOf(start)

    return shortest