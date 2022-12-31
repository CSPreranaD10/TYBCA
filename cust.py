#Importing Libraries
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

#Loading dataset
data = pd.read_csv('customers.csv')
data.head()

#Data Preprocessing
X = data.iloc[:, [3, 4]].values

#Creating Linkage Matrix
Z = linkage(X, 'ward')

#Plotting the Dendrogram
plt.title('Hierarchical Agglomerative Clustering of Customers')
plt.xlabel('Customers')
plt.ylabel('Distance')
dendrogram(
    Z,
    truncate_mode='lastp',
    p=12,
    leaf_rotation=45.,
    leaf_font_size=15.,
    show_contracted=True,
)
plt.show()

#slip 20,6