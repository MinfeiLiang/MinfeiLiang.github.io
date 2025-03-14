---
title: 'Generative AI for cementitious microstructure synthesis'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin

date: '2025-03-14T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2024-03-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-Journal']

# Publication name and optional abbreviated publication name.
publication: In *Developments in the Built Environment*
publication_short: In *DIBE*

abstract: The microstructure of cement paste determines the overall performance of concrete and therefore obtaining the microstructure is an essential step in concrete studies. Traditional methods to obtain the microstructure, such as scanning electron microscopy (SEM) and X-ray computed tomography (XCT), are time-consuming and expensive. Herein we propose using Denoising Diffusion Probabilistic Models (DDPM) to synthesize realistic microstructures of cement paste. A DDPM with a U-Net architecture is employed to generate high-fidelity microstructure images that closely resemble those derived from SEM. The synthesized images are subjected to comprehensive image analysis, phase segmentation, and micromechanical analysis to validate their accuracy. Findings demonstrate that DDPM-generated microstructures not only visually match the original microstructures but also exhibit similar greyscale statistics, phase assemblage, phase connectivity, and micromechanical properties. This approach offers a cost-effective and efficient alternative for generating microstructure data, facilitating advanced multiscale computational studies of cement paste properties.


# Summary. An optional shortened abstract.
summary: This paper presents my first attempt at using generative AI to synthesize microstructures of cementitious materials. A Denoising Diffusion Probabilistic Model (DDPM) was employed to generate synthetic BSE images of OPC with a water-to-cement ratio (w/c) of 0.4. The generated images closely resemble real BSE images in both statistical and microstructural analyses. I have recently extended this work to the conditional generation of three-dimensional hydrating cementitious microstructures with varying w/c ratios, Blaine values, and curing ages. Stay tuned for further updates!

tags:
  - Experimental and numerical study for Early-Age Stress

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links: https://www.sciencedirect.com/science/article/pii/S2666165925000249
# - name: Custom Link
#   url: http://example.org


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false
---


The denoising process of generating a cement microstructure from Gaussian noise:
![Image 1](featured1.jpg)
The stress-strain curves of generated and original microstructures obtained from Lattice Fracture Models:
![Image 2](featured2.jpg)

# Full paper access. 
The full paper can be found [here](https://www.sciencedirect.com/science/article/pii/S2666165925000249).
