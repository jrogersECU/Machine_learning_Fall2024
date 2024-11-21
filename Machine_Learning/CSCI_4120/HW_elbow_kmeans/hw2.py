from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.datasets import make_blobs
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment
import numpy as np

X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

# COMPLETE determine the best k for k-means (Completed)
model = KMeans(random_state=0)
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(X)
visualizer.show()

# COMPLETE calculate accuracy for best K (Completed)
best_k = visualizer.elbow_value_
kmeans = KMeans(n_clusters=best_k, random_state=0)
y_pred = kmeans.fit_predict(X)

# Remapped predicted labels to true labels for accurate comparison
def remap_labels(y_true, y_pred, num_clusters):
    cost_matrix = np.zeros((num_clusters, num_clusters))
    for i in range(num_clusters):
        for j in range(num_clusters):
            cost_matrix[i, j] = -np.sum((y_true == i) & (y_pred == j))
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    mapping = {col: row for row, col in zip(row_ind, col_ind)}
    return np.array([mapping[label] for label in y_pred])

y_pred_mapped = remap_labels(y_true, y_pred, best_k)


y_pred = kmeans.fit_predict(X)
accuracy = accuracy_score(y_true, y_pred_mapped)
print(f"Accuracy for best K ({best_k}): {accuracy:.2f}")


# COMPLETE draw a confusion matrix (Completed)
cm = confusion_matrix(y_true, y_pred_mapped)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_true))
disp.plot(cmap='viridis')
plt.show()