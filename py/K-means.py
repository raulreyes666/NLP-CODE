import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD

# Supongamos que df_featuresets es tu matriz de características, puedes reemplazarla con tus propios datos
# Aquí se utiliza una matriz de características aleatoria como ejemplo
n_samples = 100  # Número de muestras
n_features = 10  # Número de características
df_featuresets = np.random.rand(n_samples, n_features)

true_k = 4

truncatedSVD = TruncatedSVD(n_components=2)
X_2D = truncatedSVD.fit_transform(df_featuresets)

kmeans = KMeans(n_clusters=true_k,
                init='k-means++',
                max_iter=100,
                n_init=10)

result = kmeans.fit(X_2D)
labels = result.labels_

cm = plt.get_cmap('Accent')

for cluster in range(true_k):
    current_color = cm(1. * cluster / (true_k))
    plt.scatter(X_2D[labels == cluster, 0], X_2D[labels == cluster, 1],
                color=current_color, label='cluster ' + str(cluster))

plt.rcParams["figure.figsize"] = (20, 20)
plt.rcParams['font.size'] = '12'
plt.show()
