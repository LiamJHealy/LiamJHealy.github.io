---
layout: post
title: List Comprehension
description: "Python Programming"
tags: []
categories: [Programming]

---

List comprehension is a neat was to constuct a list in python within one line of code. The code below shows the general syntax for appending items using a loop.

{% highlight python %}
for item in iterable:
  if condition == True:
    newlist.append(x)
{% endhighlight %}

By using list comprehension, this code can be reduced to:

{% highlight python %}
newlist = [expression for item in iterable if condition == True]
{% endhighlight %}

<!-- more -->

A solution to this problem using list comprehension is the funtion <code>firstUniqChar(s)</code> shown below:

{% highlight python %}
def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return -1

        elif len(s) == 1:
            return 0

        else:
            idx = [s.index(x) for x in 'abcdefghijklmnopqrstuvwxyz' if s.count(x) == 1]
            return min(idx)
{% endhighlight %}

The funtion <code>firstUniqChar(s)</code> takes a string <code>s</code> as the input. If the length of the string is 0 or 1 then the solution is trivial. In the case when there are multiple letters in the string, we use list comprehension to loop through each letter of the alphabet <code>x in 'abcdefghijklmnopqrstuvwxyz'</code> and keep the indices <code>s.index(x)</code> where the letter only occurs once <code>s.count(x) == 1</code>. However, since we are traversing the letters in alphabetical order, we need to take the minimum index as the solution <code>return min(idx)</code>.

{% highlight python %}
firstUniqChar(s = 'aabbdc')
{% endhighlight %}

In this example, the indices which are unique are returned as follows <code>idx = [5,4]</code>. By taking the minimum of this list we gauruntee to return the first unique letter <code>d</code>, even though its not the first unique intex returned.



