---
title: 'Generative AI for cementitious microstructure synthesis'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin

date: '2025-03-15T00:00:00Z'
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
summary: This paper presents my first attempt to use generative AI for synthesizing microstructures of cementitious materials. The DDPM (Denoising Diffusion Probablistic Model) was first used to generate "fake" BSE images of OPC with w/c = 0.4. The results almost assembles the real BSE images in statistical and microstructural analysis. 

tags:
  - Experimental and numerical study for Early-Age Stress

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


The denoising process of generating a cement microstructure from Gaussian noise:
![Image 1](featured1.jpg)
The stress-strain curves of generated and original microstructures obtained from Lattice Fracture Models:
![Image 2](featured2.jpg)
