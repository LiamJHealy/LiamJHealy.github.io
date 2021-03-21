---
layout: post
title: Correlation and Dependence
description: "Mathematics and Quantitative Finance"
tags: []
categories: [Research]
comments: false
---

An important topic in statistics, especially when understanding the behaviour between variables or distributions, is the concept of dependence (or independence). One of the most useful measures of dependence is Pearson's $$\rho$$. Pearson's correlation is well known and used in the industry, however it does have its limitation; particularly when measuring the relationship between non-linear distributions or where distributions are fat-tailed.

$$
\begin{align}\notag
\text{Independence} &\Rightarrow \text{No Correlation} \\
\text{No Correlation}  &\nRightarrow \text{Independence}
\end{align}
$$

This article discusses the connection between dependence and correlation in detail and provides an example to show that having no correlation does not imply independence.

<!-- more -->

## Correlation

Pearson's Correlation $$\rho$$ is a measure of linear relationship between distribution, say $$X$$ and $$Y$$. A Pearson product-moment correlation coefficient attempts to establish a line of best fit through a set of distributions by minimising the sum of the distances between the line of best fit and the individual variants or data points. 

Consider two random variables $$X$$ and $$Y$$ with expected values $$E(X)$$ and $$E(Y)$$ and standard deviation $$\sigma_X$$ and $$\sigma_Y$$:

$$
\rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{E(XY) - E(X)E(Y)}{\sqrt{E(X^2)-E(X)^2} \cdot \sqrt{E(Y^2)-E(Y)^2}}
$$

## Independence

Assuming $$X$$ and $$Y$$ are independent, then the following properties hold by definition:

$$
\begin{equation}
\begin{split}
E(XY) &= E(X)E(Y)\\
\text{cov}(X,Y) &= E(XY) - E(X)E(Y)
\end{split}
\end{equation}
$$ 

By substituting $$E(XY) = E(X)E(Y)$$ into the equation for $$\rho_{X,Y}$$ we find that the numerator is zero. Therefore, by definition, if $$X$$ and $$Y$$ are independent then they also have zero Pearson's correlation.

$$
\boxed{\text{Independence} \Rightarrow \text{No Correlation}}
$$

## Example with Zero Correlation

Consider the example where $$X \sim N(0,1)$$ and $$Z$$ has the probability mass function:

$$
\begin{align}
P(Z=1) &= 0.5 \\
P(Z=-1) &= 0.5
\end{align}
$$

The expected value of $$Z$$ in this example is therefore equal to zero.

$$
E(Z) = \sum_{i=1}^{k}z_ip_i = (1)(0.5) + (-1)(0.5) = 0
$$

Now consider $$Y = ZX$$, i.e. $$Y$$ and $$X$$ are dependent. The cumulative distribution of $$Y$$ can be derived as follows:

$$
\begin{align}
P(Y < x) &= P(ZX < x|Z = 1)P(Z = 1) \\
         & \ \ \ \ + P(ZX < x|Z = -1)P(Z = -1) \\
         &= P(X < x)(0.5) + P(-X < x)(0.5) \\
         &= (0.5)(P(X < x) + P(X \ge -x)) \\
         &= (0.5)(P(X < x) + P(X < x)) \\
         &= P(X < x)
\end{align}
$$

which means that $$Y$$ and $$X$$ are the same distribution. 

$$
\begin{align}
\rho &= \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y} \\
       &= \text{cov}(X,Y) \\
       &= \text{cov}(X,XZ) \\
       &= E(XZX)-E(X)E(ZX) \\
       &= E(X^2Z)-E(X)E(ZX) \\
       &= E(X^2)E(Z)-E(X)^2E(Z) \\
       &= 0
\end{align}
$$

since $$E(Z) = 0$$. This demonstrates an example where both $$X$$ and $$Y$$ are $$N(0,1)$$ with correlation coefficient $$\rho = 0$$. Therefore this proves thats hacing a correlation of zero does not mean that the distributions are independent

$$
\boxed{\text{No Correlation}  \nRightarrow \text{Independence}}
$$

## Summary

In summary we have shown that dependence and correlation are not the same thing. Pearson's correlation measures the linear relationship between two variables, while dependence tells us if there is any relationship between the variables at all. We also showed an example of two distributions which have dependency on each other but also have zero correlation.p