---
title: 'Active Learning for Stress Evolution Prediction'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin

date: '2022-12-01T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2022-12-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-Journal']

# Publication name and optional abbreviated publication name.
publication: In *Computer-Aided Civil and Infrastructural Engineering*
publication_short: In *CACAIE*

abstract: Early‐age stress (EAS) is an important index for evaluating the early‐age cracking risk of concrete. This paper encompasses a thermo‐chemo‐mechanical (TCM) model and active ensemble learning (AEL) for predicting the EAS evolution. The TCM model provides the data for the AEL model. First, based on Fourier's law, Arrhenius’ equation, and rate‐type creep law, a TCM model is built to simulate the heat transfer, cement hydration, and viscoelasticity, which together determine the EAS evolution. Then, a material model composed of an eXtreme Gradient Boosting model and adjusted Model Code 2010 is built to allow for parametric study and database construction. Finally, an AEL framework is built, which incorporates principal component analysis (PCA), Gaussian process, and light gradient boosting machine (LGBM). This study resulted in the following findings. (1) The dimensionality of the 672‐by‐1 EAS vector can be effectively reduced by PCA, and the first principal component (PC) is a global index representing the magnitude of the EAS; (2) the mechanical field of the TCM model is validated by testing data. Correlation analysis on the first PC quantifies the influence of various input parameters of the TCM model, which is in accordance with common understandings of the EAS evolution process. (3) The AEL and one‐shot ensemble learning (OSEL) both achieve high prediction performance in the testing set, whose <italic>R</italic> <sup>2</sup> reaches 0.961 and 0.948, respectively. Thanks to the uncertainty‐based query procedure, comparing with OSEL, AEL shows advantages in prediction performance over the whole training history. (4) AEL can significantly reduce the number of samples required for training, which can be a major improvement in efficiency considering the computational cost of the TCM model.

# Summary. An optional shortened abstract.
summary: An active ensemble learning is constructed to efficiently predict the early-age stress evolution based on a themo-chemo-mechanical model, light gradient boosting model, and gaussian process.

tags:
  - Machine Learning for Early-Age Stress

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false
---

# Thesis Details

Thesis on _Stress evolution in early-age concrete considering autogenous deformation and creep: New experimental and modelling techniques_. Supervised by [Prof Erik Schlangen](https://www.erikschlangen.net/) and [Prof Branko Šavija](https://www.tudelft.nl/en/staff/b.savija/).

The Thermo-Chemo-Mechanical Model for early-age stress evolution:
![Image 1](featured1.jpg)
Some nice results:
![Image 2](featured1.jpg)
