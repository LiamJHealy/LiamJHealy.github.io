graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = set()

def dfs_no_recursive(visited, graph, node):

    stack = [node]

    while(len(stack) > 0):

        s = stack.pop()

        if s not in visited:
            print(s)
            visited.add(s)

            for neighbour in graph[s]:
                stack.append(neighbour)

dfs_no_recursive(visited, graph, 'A')


visited = set()

def dfs_recursion(visited, graph, node):

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            dfs_recursion(visited, graph, neighbour)

dfs_recursion(visited, graph, 'A')

# initialise an empty visited set
visited = set()

def bfs(visited, graph, node):
    '''
    :type visited: set
    :type graph: dictionary
    :type note: string
    :rtype: None
    '''

    # initialise an empty queue list
    queue = []
    visited.add(node)
    queue.append(node)

    # while the queue is not empty
    while queue:

        # pop the first element in the queue
        s = queue.pop(0) 

        # add each unvisited neighbour to the end of the queue
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# execute the function
bfs(visited, graph, 'A')