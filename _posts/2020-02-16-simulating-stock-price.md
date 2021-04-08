---
layout: post
title: Geometric Brownian Motion
description: "Research"
tags: []
categories: [Research]

---

The movement of stock prices are generally considered to be a random walk which are very difficult to accurately forecast. Because of the randomness associated with stock price movements, they need to be simulated using Stochastic Differential Equations (SDE). Geometric Brownian Motion (GBM) is one of the most common models for simulating the dynamics of stock prices because of the following properties:

- Log-Normal random path meaning that the simulated stock price cannot become negative;
- There is a drift and diffusion component which can be calibrated to historical rates;
- Closed-form solutions exist which makes simulating forward paths computationally efficient.

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

{:.center}
*Geometric Brownian Motion SDE*

where $$S$$ is the stock price, $$\mu$$ is the drift coefficient, $$\sigma$$ is the diffusion coefficient, and $$W_t$$ is the Brownian Motion.

<!-- more -->

## Brownian Motion

In order to simulate stock prices using the GBM model, we first need to model the Brownian Motion.  This is done by first sampling random variates from a standard normal distribution $$N(0,1)$$ to calculate the Brownian increments. The Brownian Path is then determined by taking the cumulative sum of the Brownian Increments. The code below demonstrates how this can be implemented in Python.


{% highlight python %}
def brownianMotion(sims, T, dt, seed):

    '''
    int sims    : number of simulations
    int T       : number of time points to predict
    float dt    : time increment
    return b, W : b - Brownian increment, W - Brownian path
    '''

    np.random.seed(seed)
    N = int(T / dt)
    b = np.random.normal(0, 1, (sims, N))*np.sqrt(dt)
    W = np.cumsum(b, axis=1)

    return b, W
{% endhighlight %}

{:.center}
![brownian-motion]({{ site.url }}/images/research/brownian-motion.png#center)

TBC


