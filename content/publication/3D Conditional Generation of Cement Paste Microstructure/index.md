---
title: '3D Conditional Generation of Cement Paste Microstructure'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin

date: '2025-07-11T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2025-07-11T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-Journal']

# Publication name and optional abbreviated publication name.
publication: In *Materials & Design*
publication_short: In *M&D*

abstract: Portland cement paste has a highly heterogenous evolving microstructure that complicates the development of stronger and greener cementitious materials. Microstructure is the fundamental input of multiscale studies on material behaviors. Herein, we propose a conditional generative AI framework for synthesizing high-fidelity 3D microstructures of hydrating cement paste (1–28 days) with varying water-to-cement ratios and Blaine fineness values. A latent diffusion transformer, operating within a compact two-stage latent space derived via a vector quantized variational autoencoder, efficiently captures and reproduces experimentally measured microstructural patterns. Statistical analyses confirm strong consistency in grey value distributions, micromechanical properties, hydration phase evolution, and particle size distributions, with only minor boundary-related discrepancies. Validation using a pretrained classifier further corroborates the fidelity of generated microstructures. This approach provides a robust tool for realistic cement paste microstructure generation, supporting multiscale modeling and advancing the design of sustainable cementitious materials.


# Summary. An optional shortened abstract.
summary: This paper is extended from previous one on 2D unconditional generation of cement paste. We proposed a latent diffusion transformer for generating the 3D microstructure of cement paste with different Blaine values, wc ratios, and ages!!! Promising results show great potential of generative AI in replacing the expensive SEM/ CT tests!

tags:
  - AI-enhanced material design

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links: https://www.sciencedirect.com/science/article/pii/S0264127525006719
# - name: Custom Link
#   url: http://example.org


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false
---

This paper is extended from previous 2D unconditional generation of cement paste. We proposed a latent diffusion transformer for generating the microstructure of cement paste with different Blaine values, wc ratios, and ages!!! Promising results show great potential of generative AI in replacing the expensive SEM/ CT tests!


The generated 3D cement paste microcubes which visually assembling the real microstructures:
![Image 1](feature1.png)
The greyvalue statistics of real and generated microstructures are almost the same!!!
![Image 2](feature2.png)

# Full paper access. 
The full paper can be found [here](https://www.sciencedirect.com/science/article/pii/S2666165925000249).
