# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:28:42 2023

@author: Korisnik
"""

###### Using Principal Component Analysis.#############

import numpy as np
from sklearn.decomposition import PCA  #Package for statistical models

# Generate a random dataset with 5 features #For 5 features we will need 5 columns, in Python from 0 in 4 
X = np.random.randn(1000, 5)

# Create a PCA object with 2 components
pca = PCA(n_components=2)

# Fit the PCA model to the data and transform the data
X_pca = pca.fit_transform(X)

# Print the shape of the original data and the transformed data
print("Original shape:", X.shape)
print("Transformed shape:", X_pca.shape)
