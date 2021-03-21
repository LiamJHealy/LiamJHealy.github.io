---
layout: post
title: European Option Delta Derivation
description: "Mathematics and Quantitative Finance"
tags: []
categories: [Research]
comments: false
---

This article derives the delta $$\Delta$$ of a European option on a non-dividend paying stock and discusses the implementation in Python.

<!-- more -->

## Delta of a European Call Option

The value of a call option for a non-dividend-paying underlying stock is

$$
\begin{align}
C_t(S_t,t) &= S_t N(d_1) - Xe^{-r(T-t)}N(d_2) \\
d_1 &= \frac{ \ln{ \left(\frac{S_t}{X}\right) } + \left( r + \frac{\sigma^2}{2}\right)(T-t)}{\sigma\sqrt{(T-t)}} \\
d_2 &= \frac{ \ln{ \left(\frac{S_t}{X}\right) } + \left( r - \frac{\sigma^2}{2}\right)(T-t)}{\sigma\sqrt{(T-t)}}
\end{align}
$$

Where:

- $$N(\cdot)$$ - is the cumulative standard normal distribution
- $$T$$ - is the time to maturity
- $$S_t$$ - is the spot price of the underlying asset at time $$t$$ 
- $$X$$ - is the strike price
- $$r$$ - is the risk free interest rate
- $$\sigma$$ - is the volatility of the underlying asset returns

The delta $$\Delta$$, is defined as the change in value of the option $$V$$ with respect to the price of the underlying asset $$S$$.

$$
\begin{align}
\Delta = \frac{\partial C_t}{\partial S_t} &= \frac{\partial S_tN(d_1)}{\partial S_t} - Xe^{-r(T-t)} \frac{\partial N(d_2)}{\partial S_t} \\
&= \frac{\partial [S_t N(d_1)]}{\partial S_t} - Xe^{-r(T-t)} \frac{\partial N(d_2)}{\partial S_t}
\end{align}
$$

To evaluate the first term in this equation we can use the product rule and the chain rule.

$$
\begin{align}
\frac{\partial S_tN(d_1)}{\partial S_t} &= \frac{\partial S_t}{\partial S_t} N(d_1) + S_t \frac{\partial N(d_1)}{\partial S_t} \hspace{0.5cm} \text{(Product Rule)}\\
&= N(d1) + S_t \frac{\partial N(d1)}{\partial d_1} \frac{\partial d_1}{\partial S_t} \hspace{0.5cm} \text{(Chain Rule)}
\end{align}
$$

Since 

$$
N(d_1) = \int_{-\infty}^{d_1} \frac{1}{\sqrt{2\pi}} e^{-\frac{X^2}{2}} dx
$$

we can evaluate the first term of the chain rule as

$$
\frac{\partial N(d_1)}{\partial d_1} = \frac{1}{\sqrt{2\pi}}e^{-\frac{d_1^2}{2}}
$$

We can also rewrite $$d_{1,2}$$ conveniently to evaluate the second term of the chain rule $$\frac{\partial d_1}{\partial S_t}$$

$$
d_{1,2} = \frac{\ln{\left(\frac{S_t}{X}\right)}}{\sigma\sqrt{T-t}} + \frac{\left( r \pm \frac{\sigma^2}{2} \right)(T-t)}{\sigma\sqrt{T-t}}
$$

$$
\therefore \frac{\partial d_1}{\partial S_t} = \frac{\partial d_2}{\partial S_t} = \frac{1}{S_t \sigma\sqrt{T-t}}
$$

By substituting all of these back into our original equation we have

$$
\Delta = N(d_1) + S_t \frac{\partial N(d_1)}{\partial S_t} - Xe^{-r(T-t)}\frac{\partial N(d_2)}{\partial S_t}
$$

And therefore $$\Delta = N(d_1) > 0$$ since it can be shown that

$$
S_t \frac{\partial N(d_1)}{\partial S_t} = Xe^{-r(T-t)}\frac{\partial N(d_2)}{\partial S_t}
$$

The Python code to calculate the delta for a European Call option on a non-dividend paying stock would be

{% highlight python %}
from scipy.stats import norm
from math import log, sqrt

def call_delta(S, v, X, T, r):
    '''
    S: Stock Price
    v: Volatility
    X: Strike Price
    T: Time to maturity
    r: Risk free interest rate
    '''

    d1 = (log(S / X) + (r + 0.5 * v**2) * T) / (v * sqrt(T))
    return norm.cdf(d1)
{% endhighlight %}
{:.center}
*European Call Option Delta*

## Delta of a European Put Option

The price of a European Put option, based on put-call parity is shown below:

$$
\begin{align}
P(S_t,t) &= Xe^{-rT} - S_t + C(S_t,t) \\
&= Xe^{-rT}N(-d_2) - S_tN(-d_1)
\end{align}
$$
