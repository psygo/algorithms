# Example Graph
graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2}, \
         'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}

def dijkstra(graph,start,goal):
    '''
    dijkstra(graph,start,goal)
    '''
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                # This is just so the first node is assigned to the start.
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                # Here we take the node with the minimum distance in
                # the previous iteration, which has been popped out.
                minNode = node

        for childNode, weight in graph[minNode].items():
            # Now we will see if there is a shorter distance going through
            # the minNode to the childNode.
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode

        unseenNodes.pop(minNode)

    print(f'The shortest distance to each note is: {shortest_distance}')

    # Now we trace back our route from the goal to the start.
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable.')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print(f'And the path from "{start}" to "{goal}" is ' + str(path))

dijkstra(graph, 'a', 'e')
