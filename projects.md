---
layout: page
title: Projects
permalink: /projects/
---

### [Poisson-Gaussian Holographic Phase Retrieval with Score-based Image Prior](https://github.com/ZongyuLi-umich/2023-PGPR) 
This study focuses on holographic phase retrieval in situations where the measurements are degraded by a combination of Poisson and Gaussian noise, as commonly occurs in optical imaging systems. We propose a new algorithm called “AWFS" that uses accelerated Wirtinger flow (AWF) with a learned score function as a generative prior. Specifically, we formulate the PR problem as an optimization problem that incorporates both data fidelity and regularization terms. We calculate the gradient of the log-likelihood function for PR and determine its corresponding Lipschitz constant. Additionally, we introduce a generative prior in our regularization framework by using score matching to capture information about the gradient of image prior distributions.

### [DblurDoseNet](https://pubmed.ncbi.nlm.nih.gov/34882821/)
Current methods for patient-specific voxel-level dosimetry in radionuclide therapy suffer from a trade-off between accuracy and computational efficiency. Monte Carlo (MC) radiation transport algorithms are considered the gold standard for voxel-level dosimetry but can be computationally expensive, whereas faster dose voxel kernel (DVK) convolution can be suboptimal in the presence of tissue heterogeneities. Furthermore, the accuracies of both these methods are limited by the spatial resolution of the reconstructed emission image. To overcome these limitations, we consider a single deep convolutional neural network (CNN) with residual learning (named DblurDoseNet) that learns to produce dose-rate maps while compensating for the limited resolution of SPECT images.

## Other Projects

### [Reducing SPECT acquisition time by predicting missing projections with single-scan self-supervised coordinate-based learning](https://jnm.snmjournals.org/content/64/supplement_1/P1014.abstract)

  SPECT acquisition under low-count conditions such as encountered in Lu-177 imaging can take 20-30 mins per field-of-view with standard systems, which is particularly challenging when multiple bed positions are needed. The goal of this work is to reduce SPECT acquisition time by only acquiring a subset of total projections (e.g., 30 of 120) and then use a neural network with single-scan self-supervised coordinate-based learning to predict missing projections before reconstruction.
   
### [Training End-to-End Unrolled Iterative Neural Networks for SPECT Image Reconstruction](https://ieeexplore.ieee.org/abstract/document/10032177)

   We implemented an open-source, high-performance Julia implementation of a SPECT forward–backward projector that supports memory-efficient backpropagation with an exact adjoint. Our Julia projector uses only ~5% of the memory of an existing MATLAB-based projector. We compare unrolling a CNN-regularized expectation–maximization (EM) algorithm with end-to-end training using our Julia projector with other training methods, such as gradient truncation (ignoring gradients involving the projector) and sequential training, using XCAT phantoms and virtual patient (VP) phantoms generated from SIMIND Monte Carlo (MC) simulations.

## Contact me

[zonyul@umich.edu](mailto:zonyul@umich.edu)
