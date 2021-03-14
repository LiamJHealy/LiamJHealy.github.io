---
layout: post
title: Mathematics of Copulas
description: "Mathematics and Quantitative Finance"
tags: []
categories: [Research]
comments: false
---

This article discusses the mathematics of the Gaussian and t-Copula. Refer to the programming articles to see how to create a function to create a Gaussian and t-Copua in practice...

<!-- more -->

### Original Yolo V3 ###

The architecture of the original Yolo V3 looks like this:

![Yolo V3 Architecture]({{ site.url }}/images/machine_learning/gaussian_yolo/yolo_output.jpg)

There are detection outputs(Yolo layer) from 3 difference scales, the uncertainty estimation is applied for all 3 Yolo layers, this blog will only explain the Yolo layer of the 2nd scale. The 94th layer consists of the regression channels for bounding box localization(channel $$t_x$$ ,$$t_y$$, $$t_w$$ and $$t_h$$), the confidence map of objectness and the classification channels for different classes($$P_0$$ ,$$P_1$$ ....).

Based on the detection encoding of Yolo V3, each pixel of a Yolo layer represent a grid cell, $$t_x$$ and $$t_y$$ represent the coordinates of the bounding box center within a grid cell, thus their ranges must be between 0 and 1. As an example, if the bounding box center is located at the center of a grid cell, both $$t_x,t_y$$ will be 0.5. In order to make sure that the regressed value does not exceed the range, a sigmoid activation layer is used to regress $$t_x, t_y$$.

For $$t_w, t_h$$, they are used to encode the width and height of the bounding box based on the prior:

$$
b_w=p_we^{t_w}\\
b_h=p_he^{t_h}
$$
