---
title: 'Finding Structure with Randomness: Probabilistic Algorithms for Constructing
  Approximate Matrix Decompositions'
authors:
- N. Halko
- P. G. Martinsson
- J. A. Tropp
date: '2011-01-01'
publishDate: '2024-06-17T14:55:15.081972Z'
publication_types:
- article-journal
publication: '*SIAM Review*'
doi: 10.1137/090771806
abstract: Low-rank matrix approximations, such as the truncated singular value decomposition
  and the rank-revealing QR decomposition, play a central role in data analysis and
  scientific computing. This work surveys and extends recent research which demonstrates
  that randomization offers a powerful tool for performing low-rank matrix approximation.
  These techniques exploit modern computational architectures more fully than classical
  methods and open the possibility of dealing with truly massive data sets. This paper
  presents a modular framework for constructing randomized algorithms that compute
  partial matrix decompositions. These methods use random sampling to identify a subspace
  that captures most of the action of a matrix. The input matrix is then compressed-either
  explicitly or implicitly-to this subspace, and the reduced matrix is manipulated
  deterministically to obtain the desired low-rank factorization. In many cases, this
  approach beats its classical competitors in terms of accuracy, robustness, and/or
  speed. These claims are supported by extensive numerical experiments and a detailed
  error analysis. The specific benefits of randomized techniques depend on the computational
  environment. Consider the model problem of finding the k dominant components of
  the singular value decomposition of an m × n matrix. (i) For a dense input matrix,
  randomized algorithms require O(mn log(k)) floating-point operations (flops) in
  contrast to O(mnk) for classical algorithms. (ii) For a sparse input matrix, the
  flop count matches classical Krylov subspace methods, but the randomized approach
  is more robust and can easily be reorganized to exploit multiprocessor architectures.
  (iii) For a matrix that is too large to fit in fast memory, the randomized techniques
  require only a constant number of passes over the data, as opposed to O(k) passes
  for classical algorithms. In fact, it is sometimes possible to perform matrix approximation
  with a single pass over the data. © 2011 Society for Industrial and Applied Mathematics.
links:
- name: URL
  url: http://epubs.siam.org/doi/10.1137/090771806
---
