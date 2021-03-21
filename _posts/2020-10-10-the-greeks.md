---
layout: post
title: The Greeks
description: "Mathematics and Quantitative Finance"
tags: []
categories: [Research]
comments: false
---

The Greeks are used describe the different dimensions of risk involved in taking an options position in the market. These dimensions are referred to as Greeks because they are represented by Greek symbols such as delta, theta, vega, etc. Greeks are used to measure and monitor the sensitivity of an option in the market which helps to manage the risk of an options portfolio.

$$
\Delta = \frac{\partial V}{\partial S}, \hspace{0.5cm} \Theta = \frac{\partial V}{\partial \tau}, \hspace{0.5cm} \nu = \frac{\partial V}{\partial \sigma}, \hspace{0.5cm} \rho = \frac{\partial V}{\partial r}
$$

{:.center}
*First Order Greeks*

<!-- more -->

The Black-Scholes model is a partial differential equation (PDE) which is a multivariate function that explains the value of an option given changes in other intrinsic and market parameters. The Greeks are simply the sensitivity of the PDE to changes in the parameters. Many PDE are difficult to solve or are computationally expensive, however, the Black-Scholes model has been thoroughly researched and there are known closed for solution which reduce the computation expense to compute these metrics.

## Black-Scholes Equation

The Black-Scholes equation is used to value options based on a no arbitrage argument. The Black-Scholes equation takes the form

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2
S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0$$

## Gradient

In mathematics, the partial derivatives of a PDE are referred to as the gradient $$\nabla$$ of the function. Consider the function with $$n$$ parameters

$$
f(x_1, x_2, \dots, x_n)
$$

The gradient of this function would therefore be

$$
\nabla f(x_1, x_2, \dots, x_n) = \Bigg \langle \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \Bigg \rangle
$$

Within the Black-Scholes model, there are four parameters which can be determined from the gradient using closed form solution for European Call and Put option. However, exotic options don't always have closed form solutions and therefore differential solvers may be required which are often computationally expensive.

## The Greeks
The four variables in the Black-Scholes model are as follows. The value of the derivative (call/put) is represented by $$V$$.

- Delta - $$\Delta$$ - First partial derivative of the option value w.r.t the asset price $$\frac{\partial V}{\partial S}$$
- Theta - $$\Theta$$ - First partial derivative of the option value w.r.t time $$\frac{\partial V}{\partial \tau}$$
- Vega - $$\nu$$ - First partial derivative of the option value w.r.t the asset volatility $$\frac{\partial V}{\partial \sigma}$$
- Rho - $$\rho$$ - First partial derivative of the option value w.r.t the interest rate $$\frac{\partial V}{\partial r}$$

