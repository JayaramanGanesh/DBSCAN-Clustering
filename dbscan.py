import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# ... (Previous code remains the same)

# Plot up the results!
min_x = np.min(data[:, 0])
max_x = np.max(data[:, 0])
min_y = np.min(data[:, 1])
max_y = np.max(data[:, 1])

fig = plt.figure(figsize=(12, 6))

# Plot the original data
plt.subplot(121)
plt.scatter(data[:, 0], data[:, 1], c='black', marker='o', s=10)
plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.title('Original Data', fontsize=20)

# Plot the clusters and outliers
plt.subplot(122)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise (outliers).
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = data[class_member_mask & core_samples_mask]
    plt.scatter(xy[:, 0], xy[:, 1], c=[col], marker='o', s=50, edgecolor='k', label='Cluster %d' % k)

    xy = data[class_member_mask & ~core_samples_mask]
    plt.scatter(xy[:, 0], xy[:, 1], c=[col], marker='o', s=20, edgecolor='k')

plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.title('DBSCAN: %d clusters found' % n_clusters, fontsize=20)

# Add a legend to show cluster colors
plt.legend(loc='lower right', fontsize=10)

fig.tight_layout()
plt.subplots_adjust(left=0.03, right=0.98, top=0.9, bottom=0.05)
plt.show()
