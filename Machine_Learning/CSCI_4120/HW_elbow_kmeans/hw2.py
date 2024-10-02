from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.datasets import make_blobs
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

# TODO determine the best k for k-means (Completed)
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(X)
visualizer.show()

# TODO calculate accuracy for best K (Completed)
best_k = visualizer.elbow_value_
kmeans = KMeans(n_clusters=best_k)
y_pred = kmeans.fit_predict(X)
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy for best K ({best_k}): {accuracy}")

# TODO draw a confusion matrix (Completed)
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()