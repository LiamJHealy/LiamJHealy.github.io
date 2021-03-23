---
layout: post
title: Deriving Delta for European Options
description: "Mathematics and Quantitative Finance"
tags: []
categories: [Research]
comments: false
---

This article derives the delta $$\Delta$$ of a European option on a non-dividend paying stock and discusses the implementation in Python.

<!-- more -->

## Delta of a European Call: $$\Delta_c$$

The value of a call option for a non-dividend-paying underlying stock is

$$
C_t(S_t,t) = S_t N(d_1) - Xe^{-r(T-t)}N(d_2) \label{eq1}\tag{1}
$$

where

$$
N(d) = \frac{1}{\sqrt{2\pi}}\int_{\infty}^d e^{-\frac{s^2}{2}}ds, \label{eq2}\tag{2}
$$

is the cumulative distribution of a standard normal distribution,

$$
\begin{align}
d_1 &= \frac{ \ln{ \left(\frac{S_t}{X}\right) } + \left( r + \frac{\sigma^2}{2}\right)(T-t)}{\sigma\sqrt{(T-t)}} \label{eq3}\tag{3}\\
d_2 &= \frac{ \ln{ \left(\frac{S_t}{X}\right) } + \left( r - \frac{\sigma^2}{2}\right)(T-t)}{\sigma\sqrt{(T-t)}} \label{eq4}\tag{4}
\end{align}
$$

- $$(T - t)$$ - is the time to maturity
- $$S_t$$ - is the spot price of the underlying asset at time $$t$$ 
- $$X$$ - is the strike price
- $$r$$ - is the risk free interest rate
- $$\sigma$$ - is the volatility of the underlying asset returns

The delta  is defined as the change in value of the option $$V$$ with respect to the price of the underlying asset $$S$$.

$$
\Delta_c = \frac{\partial C_t}{\partial S_t} = \frac{\partial [S_t N(d_1)]}{\partial S_t} - Xe^{-r(T-t)} \frac{\partial N(d_2)}{\partial S_t} \label{eq5}\tag{5}
$$

To evaluate the first term of (\ref{eq5}) we can use a combination of the product rule and the chain rule as follows

$$
\begin{align}
\frac{\partial S_tN(d_1)}{\partial S_t} &= \frac{\partial S_t}{\partial S_t} N(d_1) + S_t \frac{\partial N(d_1)}{\partial S_t} \label{eq6}\tag{6} \\
&= N(d1) + S_t \frac{\partial N(d_1)}{\partial d_1} \frac{\partial d_1}{\partial S_t} \label{eq7}\tag{7}
\end{align}
$$

We can evaluate the first partial derivative in (\ref{eq7}) as 

$$
\frac{\partial N(d_i)}{\partial d_i} = \frac{1}{\sqrt{2\pi}} \frac{\partial}{\partial d_i} \int_{-\infty}^{d_i} e^{-\frac{s^2}{2}}ds = \frac{e^{-\frac{d_i^2}{2}}}{\sqrt{2\pi}} \label{eq8}\tag{8}
$$

We can also rewrite $$d_{1,2}$$ conveniently to evaluate the second partial derivative in (\ref{eq7}) as

$$
d_{1,2} = \frac{\ln{\left(\frac{S_t}{X}\right)}}{\sigma\sqrt{T-t}} + \underbrace{\frac{\left( r \pm \frac{\sigma^2}{2} \right)(T-t)}{\sigma\sqrt{T-t}}}_{\text{Constant w.r.t } S_t} \label{eq9}\tag{9}
$$

and therefore

$$
\frac{\partial d_1}{\partial S_t} = \frac{\partial d_2}{\partial S_t} = \frac{1}{S_t \sigma\sqrt{T-t}} \label{eq10}\tag{10}
$$

By substituting (\ref{eq7}), (\ref{eq8}) and (\ref{eq10}) into (\ref{eq5}), we get the expression for the delta of a European call option

$$
\begin{align}
\Delta_c &= N(d_1) + \frac{e^{-\frac{d_1^2}{2}}}{\sigma\sqrt{2\pi (T-t)}} \\
& \hspace{2.2cm} - Xe^{-r(T-t)} \frac{e^{-\frac{d_2^2}{2}}}{S_t\sigma\sqrt{2\pi (T-t)}} \\
&= N(d_1) + \frac{Ee^{-\frac{d_1^2}{2}}}{S_t\sigma\sqrt{2\pi(T-t)}} \left( \frac{S}{E} - e^{-r(T-t)-\frac{d_2^2}{2}+\frac{d_1^2}{2}} \right) \label{eq11}\tag{11}
\end{align}
$$

Equation (\ref{eq11}) can be reduced further by noting that 

$$
\frac{S_t}{E} = e^{-r(T-t)-\frac{d_2^2}{2}+\frac{d_1^2}{2}}
$$

and hence

$$
\Delta_c = N(d_1)
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

## Delta of a European Put: $$\Delta_p$$

The price of a European Put option, based on put-call parity is shown below:

$$
\begin{align}
P(S_t,t) &= Xe^{-rT} - S_t + C(S_t,t) \\
&= Xe^{-rT}N(-d_2) - S_tN(-d_1)
\end{align}
$$
