---
title: Deep Learning using Rectified Linear Units (ReLU)
authors:
- Abien Fred Agarap
date: '2018-03-01'
publishDate: '2024-06-17T14:55:15.601196Z'
publication_types:
- article-journal
abstract: We introduce the use of rectified linear units (ReLU) as the classification
  function in a deep neural network (DNN). Conventionally, ReLU is used as an activation
  function in DNNs, with Softmax function as their classification function. However,
  there have been several studies on using a classification function other than Softmax,
  and this study is an addition to those. We accomplish this by taking the activation
  of the penultimate layer $h_n - 1$ in a neural network, then multiply it by weight
  parameters $þeta$ to get the raw scores $o_i$. Afterwards, we threshold the raw
  scores $o_i$ by $0$, i.e. $f(o) = max(0, o_i)$, where $f(o)$ is the ReLU function.
  We provide class predictions $haty$ through argmax function, i.e. argmax $f(x)$.
---
