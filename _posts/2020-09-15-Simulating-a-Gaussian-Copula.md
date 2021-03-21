---
layout: post
title: Gaussian Copula Simulation
description: "Mathematics and Quantitative Finance"
tags: []
categories: [Research]
comments: false
---

A Copula is a multivariate cumulative distribution function which describe the dependence between random variables. Copulas are often used in quantitative finance to model the tail-risk or returns of a set of correlated distributions (Marginal Distributions). There are many types of Copula which all have different application. The purpose of this article is to introduce the concept of marginal and joint distribution, as well as deriving the Gaussian Copula. 

<!-- more -->

## Marginal Distribution

Consider a distribution $$X$$ which we can simulate $$n$$ random variates {$$x_1, x_2, \dots, x_n$$}. Each of these random variates are independent and identically distributed since they come from the same distribution and are mutually independent. We can refer to this as the marginal distribution $$f_X(x)$$. In the case when we have $$d$$ distribution $$X_1, X_2, \dots, X_d$$, then the marginal distributions are defined as $$f_{X_1}(x_1),\dots,f_{X_d}(x_d)$$. 

The charts below show an example of a PDF and CDF for an i.i.d  distribution which is $$\text{Normal}(0,1)$$ with a sample size of $$50$$:

![sample_distribution]({{ site.url }}/images/research/sample_distribution.png)

## Joint Distribution

The correlation between margins distributions are the reason we need a Copulas, so that the dependence can be modelled. For more details on dependence and correlation, refer to the <code>Statistical Dependence</code> article. can define the correlation as:

$$
\begin{equation}
\rho =   
    \begin{pmatrix}
    \rho_{X_1X_1} & \rho_{X_1X_2} & \cdots & \rho_{X_1X_d} \\
    \rho_{X_2X_1} & \rho_{X_2X_2} & \cdots & \rho_{X_2X_d} \\
    \vdots  & \vdots  & \ddots & \vdots  \\
    \rho_{X_dX_1} & \rho_{X_dX_2} & \cdots & \rho_{X_dX_d} 
    \end{pmatrix}
\end{equation}
$$

Sklar's theorem states that every multivariate cumulative density function of random vectors $$X_1, X_2, \dots, X_d$$ can be expressed in terms of its marginal distributions $$f_{X_1}(x_1),\dots,f_{X_d}(x_d)$$. Therefore the join distribution is

$$
\begin{equation}
\underbrace{f_{X_1,\dots,X_d}(x_1,\dots,x_d)}_{\text{Joint Distribution}} = C(\underbrace{f_{X_1}(x_1) \cdot f_{X_2}(x_2) \cdots f_{X_d}(x_d)}_{\text{Marginal Distributions}})
\end{equation}
$$

where $$C$$ is the Copula.

## Simulating a Joint Distribution

In order to be able to simulate a joint distribution we need to understand the dependence structure between the marginal distribution. 

### a) Independent Margin Distributions

In the case where the marginal distributions are independent, then there is no need for a copula to determine the joint distribution. Consider the example where we have the marginal distribution $$X \sim N(0,1)$$ and $$Y \sim N(0,1)$$. The joint distribution can be expressed as:

$$
F_{X,Y}(x,y) = F_X(x) \cdot F_Y(y)
$$

The expected value and variance of $$F_{X,Y}(x,y)$$ can be calculated as follows:

$$
E(f_{X,Y}) = E(f_{X} \cdot E(f_{Y})
$$

$$
\begin{align}
\text{Var}(f_{X,Y}) &= [E(X)]^2 \text{Var}(Y)+[E(Y)]^2 \text{Var}(X) + \text{Var}(X)Var(Y) \\
&= E(X^2)E(Y^2) - [E(X)]^2[E(Y)]^2
\end{align}
$$

By simulating $$1,000$$ times we can construct a emperical joint distribution as shown below:

![independent_joint_distribution]({{ site.url }}/images/research/independent_joint_distribution.png)

### b) Dependent Margin Distributions

Now consider the example where we have the marginal distribution $X$ and $Y$ which are Standard Normal Distributions but have an element of dependence (Called a Bivariate Normal). For this example we also need to know the relationship between $X$ and $Y$ is order to determine the joint distribution.

\begin{equation}\notag
X, Y \sim N(0,1)\\
\rho = 
    \begin{bmatrix}
    1 & \rho_{XY} \\
    \rho_{XY} & 1 
    \end{bmatrix}
\end{equation}

In order to determine the joint distirbution $f_{X,Y}(x,y,\rho)$ we need to do a bit more work than the first example. Lets say that we know one of the random variates in $X$, say $x_1$. Then what does that tell us about the distribution of the next random variate from $Y$? To answer this we need to answer two questions:

1. We know the distribution of $$Y$$;
2. What are the parameters (Expected Value and Variance) of $$Y$$.

The answer to the first question is Normal because we know both $$X$$ and $$Y$$ are originally Standard Normal distributions. The parameters of $$Y$$ however, are not known staight away and will need to be determined.

**Expected Value:**

The expected value of $$y_1$$ given that we know $$x_1$$ is

\begin{equation} \notag
E(y_1|X=x_1) = \mu_Y + \underbrace{\rho \cdot \sigma_Y \cdot \left( \frac{x_1 - \mu_X}{\sigma_X} \right)}_{\text{Scaled Mean Shock}}
\end{equation}

This equation is basically saying that the expected value of $$y_1$$ given that we know $$x_1$$ is the original mean of $$Y$$ plus a shock to account for the fact that $$x_1$$ may be different than the original mean of $$X$$. Note that in the event that $$x_1=\mu_X$$ then the expectected value of $$y_1$$ would be the original mean of $$Y$$ which is $$\mu_Y$$.

**Standard Deviation:**

The standard deviation of $$y_1$$ given that we know $$x_1$$ is

$$
\begin{equation}\notag
Sd(y_1|X=x_1)=\sigma_Y \cdot \sqrt{1-\rho^2}
\end{equation}
$$

This equation tells us that the updated standard deviation of $$y_1$$, given that we know $$x_1$$ is a scaled version of the original Standard Deviation $$\sigma_Y$$. In fact, the scaling factor $$\sqrt{1-\rho^2}$$ ensures that the conditional Standard Deviation is lower than the original $$\sigma_Y$$. This makes sense because if we know more about $$X$$ means we should also know more about $$Y$$, given that they have some relationship $$\rho$$.

**Example Simulation ($$x_1=2$$)**

Lets consider the example where $$X$$ and $$Y$$ are dependent Standard Normal distribution with a pearson correlation of $$\rho_{XY} = 0.8$$ (i.e. they are 80% linearly correlation). Lets also assume that we randomly sample $$x_1=2$$ from $$X \sim N(0,1)$$. 

{:.center}
![gaussian_example]({{ site.url }}/images/research/gaussian_example.png)


## Simulating Gaussian Copula

The process to calculate $$X$$ and $$Y$$ is as follows:

1. Obtain random variates $$Z_X, Z_Y \sim N(0,1)$$ assuming indepences ($$\rho = 0$$), as we did in Section 1. Sampling Standard Normal distributions as a starting point is why we define this as a Gaussian Copula.
2. Apply the Cholesky Decomposition to $$Z_X$$ and $$Z_Y$$ to get $$X, Y \sim N(0,1)$$ such that they retain their linear dependence ($$\rho = 0.8$$)

**Step 1: Independent Random Variates**

The first step is to simply simulate $$Z_X$$ and $$Z_Y$$ from two Standard Normal Distributions independently. The charts below show that the CDFs for each distribution are similar and that there is no dependence structure due to the symetric nature of the variance.

{:.center}
![gaussian_z]({{ site.url }}/images/research/gaussian_z.png)

**Step 2: Cholesky Decomposition and Determine $$X$$ and $$Y$$**

Once we have drawn our $$Z_X$$ and $$Z_Y$$ from independent Standard Normal distribution, we now have to take into account the dependence structure between the two samples by applying Cholesky Decomposion.

For a two-dimentional correlation matrix $$\rho$$ defined as

$$
\begin{equation}\notag
\rho = 
    \begin{bmatrix}
    1 & \rho_{XY} \\
    \rho_{XY} & 1 
    \end{bmatrix}
\end{equation}
$$

The Cholesky Decomposition is

$$
\begin{equation}\notag
A =
    \begin{bmatrix}
    1 & 0 \\
    \rho_{XY} & \sqrt{1-\rho_{XY}^2} 
    \end{bmatrix}
\implies \rho = AA^T
\end{equation}
$$

Therefore we can calculate $$X$$ and $$Y$$ as follows:

$$
\begin{equation}\notag
    \begin{bmatrix}
    X \\
    Y
    \end{bmatrix}=
    \begin{bmatrix}
    1 & 0 \\
    \rho_{XY} & \sqrt{1-\rho_{XY}^2} 
    \end{bmatrix}
    \begin{bmatrix}
    Z_X \\
    Z_Y 
    \end{bmatrix} \implies
    \begin{cases}
      X &= Z_X\\
      Y &= \rho_{XY}Z_Y + \sqrt{1-\rho_{XY}^2}Z_Y
    \end{cases} 
\end{equation}
$$

the results below show that the marginal distributions of $$X$$ and $$Y$$ look the same as $$Z_X$$ and $$Z_Y$$, however the joint distribution is clearly shows the dependence structure. This demonstrates an example as to why we do not nessassarily know the join distribution given the marginal distributions. The Copula is also needed to understand the joint distribution.

{:.center}
![gaussian_chol]({{ site.url }}/images/research/gaussian_chol.png)