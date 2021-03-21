---
layout: post
title: Depth-First Search Algorithm
description: "Python Programming"
tags: []
categories: [Programming]
---

Depth-first search (DFS) algorithm is used for tree traversal on graph or tree-like data structures. It can be implemented using recursion and data structures like dictionaries and sets in Python. 

<!-- more -->

The general algorithm is as follows:

1. Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
2. Repeat until all the nodes are visited, or the node to be searched is found.

{:.center}
![dfs]({{ site.url }}/images/programming/dfs.png#center)

{:.center}
*Illustrated Depth-First Search Tree Traversal*

DFS algorithms are often implemented in the simulation of games where the number of decisions in the future could be very large, i.e. a deep tree.

The code below demonstrates the implementation of a DFS algorithm in Python. The graph above is first stored as a dictionary to illustrate this example.

{% highlight python %}
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}
{% endhighlight %}

This algorithm is implemented by defining an empty set <code>visited = set()</code> to store the value of the nodes as we traverse them. Using a set instead of a list is optimal in this case because we only intent to visit each node once and its quicker to lookup stored values in a set rather than a list (the <code>in</code> operator has a time complexity of $$O(1)$$ for a set).

For each node that that has not yet been visited, we simply add it to our visited set and continue searching its neighbours. Recursion is used to continue the search until we reach the desired node or search the whole tree

{% highlight python %}
# initialise an empty visited set
visited = set()

def dfs_no_recursive(visited, graph, node):
    '''
    :type visited: set
    :type graph: dictionary
    :type node: string
    :rtype: None
    '''

    # initiate the stack
    stack = [node]

    # continue while the stack is not empty
    while(len(stack) > 0):

        # pop the element from the end of the stack
        s = stack.pop()

        # if the node has not been visited then continue down the tree
        if s not in visited:
            visited.add(s)

            # append the neighbours to the stack
            for neighbour in graph[s]:
                stack.append(neighbour)

# execute the function
dfs_no_recursive(visited, graph, 'A')
{% endhighlight %}

{:.center}
*Depth-First Search Algorithm without Recursion*

{% highlight python %}
# initialise an empty visited set
visited = set()

def dfs_recursion(visited, graph, node):
    '''
    :type visited: set
    :type graph: dictionary
    :type node: string
    :rtype: None
    '''
    
    # continue if node has not been visited
    if node not in visited:
        visited.add(node)

        # recursively execute the function on node's neighbours
        for neighbour in graph[node]:
            dfs_recursion(visited, graph, neighbour)

# execute the function
dfs_recursion(visited, graph, 'A')
{% endhighlight %}

{:.center}
*Depth-First Search Algorithm with Recursion*

An alternative to DFS algorithms is Breadth-First search (BFS) which is cover in a different article and instead of using recursion with a stack that is executed in a first-in-last-out order, it instead creates a queue which executes in a first-in-first-out order.

The time complexity of of DFS is generally considered to be $$O(V)$$ where $$V$$ is the number of nodes.