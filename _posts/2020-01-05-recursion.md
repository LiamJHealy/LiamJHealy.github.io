---
layout: post
title: Recursion
description: "Programming"
tags: []
categories: [Programming]

---

Recursion in defined as the process of defining something in terms of itself. This means that a function can be used within its own function to create a stack which will be run in reverse order to which it is constructed (i.e. first-in-last-out). The factorial function below is a basic example of recursion in Python.

{% highlight python %}
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
{% endhighlight %}

{:.center}
*Example of Recursion to Calculate Factorial in Python*

{% highlight c++ %}
uint fibonacci(uint n) { 
	return n > 1 ? fibonacci(n-1) + fibonacci(n-2) : n; 
}  
{% endhighlight %}

{:.center}
*Example of Recursion to Calculate Factorial in C++*

<!-- more -->

## The Stack

recursion is often considered as a memory intensive process because it requires a stack which is built up recursively. For every call of the function, another element is added to the top of the stack and once the base case is reached (at the top of the stack), the element is “popped” off from the top and is passed to the value below it. The chart below illustrates the construction of the stack for the factorial example above with <code>n = 4</code>.

{:.center}
![stack]({{ site.url }}/images/programming/stack.png#center)

{:.center}
*Illustration of a Stack*

## Sorting Algorithms with Recursion

Recursion is a very useful tool to which is commonly used in the development of algorithms and recursive models. Another common example where recursion is often implemented is in sorting algorithms. More specifically, in the Merge-Sort algorithms which is illustrated below using recursion.

{:.center}
![merge-sort]({{ site.url }}/images/programming/merge-sort.png#center)

The advantage of using recursion for sorting an array is that recursion can be used to break down an unsorted array into sorted sub-arrays. It is then much less computationally expensive to merge sorted arrays. In this example we started with the unsorted array <code>[4,7,5,2]</code>. The Python code below illustrates how a Merge-Sort algorithm can be implemented in Python using recursion.

{% highlight python %}
def mergeSort(myList):

    # Continue to split the array until there is only 1 element (i.e. sorted by default)
    if len(myList) > 1:

        # Calculate the middle of the array to split
        mid = len(myList) // 2

        # Split the array into two
        left = myList[:mid]
        right = myList[mid:]

        # Recursive step
        mergeSort(left)
        mergeSort(right)

        # Merging two SORTED arrays below:
        i, j, k, = 0, 0, 0

        # Add smallest element when both sorted sub-arrays have elements
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            
            k += 1

        # Add remaining elements
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        # Add remaining elements
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1

    # Print results
    print(myList)
{% endhighlight %}

The results of this algorithm are shown below.

{% highlight python %}
[4]
[7]
[4, 7]
[5]
[2]
[2, 5]
[2, 4, 5, 7]
{% endhighlight %}

This output shows the order that the code was actually run. The recursive step in this program breaks the unsorted array down until there are two elements of length 1 (sorted by definition). The algorithm has therefore broken the problem down into merging a set of sorted arrays which is much easier to code.


## Summary

Recursion is almost certainly slower when implemented compared to iterations, however the benefits of recursion is that it often results in much more concise code which is easier to manage and understand. Another benefit of recursion is that it makes tree traversal much simpler to implement, for example in Depth-First-Search algorithms. The main negative of using recursion is that it requires more memory in order to construct and evaluate the stack.