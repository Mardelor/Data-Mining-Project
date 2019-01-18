import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from tools import load_data, usable_elts_of_size_3, usable_elts_of_size_4, usable_elts_of_size_2


def plot_pca(cleared_dataset):

    # Do the KMeans
    nb_clusters = 4
    kmeans = KMeans(n_clusters=nb_clusters, random_state=0).fit(cleared_dataset)
    print("Centres: ", kmeans.cluster_centers_)

    # The graph
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.autoscale(enable=True, axis='both', tight=None)
    ax.set_title('ACP')
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_zlabel('PC3')

    # Plot the clusters obtained
    cleared_dataset = np.array(cleared_dataset)

    pca = PCA(n_components=3)
    principal_components = pca.fit_transform(cleared_dataset)
    principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2', 'PC3'])
    principal_df = np.array(principal_df)
    ax.set_xlim(-1000, 2000)
    # ax.set_ylim(-10, 100)
    # ax.set_zlim(-10, 80)
    print(principal_df)

    listX, listY, listZ = [], [], []

    for row in range(len(cleared_dataset)):
        listX.append(principal_df[row][0])
        listY.append(principal_df[row][1])
        listZ.append(principal_df[row][2])

    variance1 = np.var(principal_components, axis=0)
    ratio = variance1 / np.sum(variance1)
    print("Importance axes: ", ratio)

    plt.plot(listX, listY, listZ, ".r")


if __name__ == "__main__":
    columns_to_use = ['serving_quantity', 'energy_100g', 'fat_100g', 'saturated-fat_100g']
    dataset = load_data(columns_to_use)
    plot_pca(dataset)
    plt.show()
