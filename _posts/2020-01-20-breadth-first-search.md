---
layout: post
title: Breadth-First Search Algorithm
description: "Python Programming"
tags: []
categories: [Programming]

---

Breadth-first search (BFS) algorithm is used for tree traversal on graph or tree-like data structures. It is implemented in python with a queue that adopts a first-in-first-out policy. 

<!-- more -->

The general algorithm for a BFS search is: 

1. Pick any node. If it is unvisited, mark it as visited and add its neighbouring nodes to the queue.
2. If there is no more remaining neighbours then remove the first node from the queue and continue until the que is empty.

{:.center}
![bfs]({{ site.url }}/images/programming/bfs.png#center)

{:.center}
*Illustrated Breadth-First Search Tree Traversal*

DFS algorithms are often implemented when the tree is wide and not very deep or when the objective is to find the shortest path to a particular node.

The code below demonstrates the implementation of a BFS algorithm in Python. The graph above is first stored as a dictionary to illustrate this example.

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

This algorithm is implemented by defining an empty set <code>visited = set()</code> to store the value of the nodes as we traverse them. Using a set instead of a list is optimal in this case because we only intent to visit each node once and its quicker to lookup stored values in a set rather than a list (the <code>in</code> operator has a time complexity of $$O(1)$$ for a set). We also initialise a queue which will hold the neighbouring nodes which have not yet been visited.

For each node that that has not yet been visited, we simply add it to our visited set and to the queue. Once a node does not have any more neighbours to add to the queue, we take the next node from the queue and continue on.

{% highlight python %}
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
{% endhighlight %}

{:.center}
*Depth-First Search Algorithm*

The time complexity of of BFS is generally considered to be $$O(V)$$ where $$V$$ is the number of nodes. Both DFS and BFS have the same average time complexity, so the decision to chose one algorithm over the other is dependent on the specific problem.