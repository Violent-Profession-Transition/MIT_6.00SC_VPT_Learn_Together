def shortestPath(graph, start, end, toPrint = False, visited = []):
    if toPrint: #for debugging
        print start, end
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]
    # add start to visited
    visited = [str(start)]
    if start == end:
        return path
    shortest = None
    for node in graph.childrenOf(start):
        if (str(node) not in visited): #avoid cycles
            visited = visited + [str(node)] #new list
            newPath = shortestPath(graph, node, end, toPrint, visited)
            if newPath == None:
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath
    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path

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

    #print("Explored DFS path: [", printPath(path), " ]")

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
            #print("returned newPath is: ", printPath(newPath))
            # if there is a path from start to end
            if newPath != None:
                global solutions
                solutions.append(newPath)
        else:
            print('Already visited', node)
    # end of for loop of childrenOf(start)

    return newPath


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
    #print("Build upon DFS path: [", printPath(path), " ]")

    # Base Case when start is end, return explored path
    if start == end:
        # start is end, path=[start]
        print("*** Reached Destination ***")
        #print("*** returned path: {} ***".format(printPath(path)))
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