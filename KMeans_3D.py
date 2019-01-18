from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tools import load_data


def plot_kmeans_3d(cleared_dataset):
    # Do the KMeans
    nb_clusters = 4
    random_state = 50
    kmeans = KMeans(n_clusters=nb_clusters, random_state=random_state).fit(cleared_dataset)
    print("Centres: ", kmeans.cluster_centers_)

    # The graph
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.autoscale(enable=True, axis='both', tight=None)
    ax.set_title('KMeans')

    # Plot the clusters obtained
    c = 0
    cleared_dataset = np.array(cleared_dataset)
    nb_col = cleared_dataset.shape[1]
    ax.set_xlabel(columns_to_use[0])
    ax.set_ylabel(columns_to_use[1])
    ax.set_zlabel(columns_to_use[2])

    listXr, listYr, listZr, listXy, listYy, listZy = [], [], [], [], [], []
    listXg, listYg, listZg, listXb, listYb, listZb = [], [], [], [], [], []
    for row in range(len(cleared_dataset)):
        data = [cleared_dataset[row][x] for x in range(nb_col)]
        data = np.array(data)
        data = data.reshape(1, -1)
        pred = kmeans.predict(data)  # For each product, we determine in which cluster it is

        if pred == 0:  # First cluster
            c += 1
            listXr.append(cleared_dataset[row][0])
            listYr.append(cleared_dataset[row][1])
            listZr.append(cleared_dataset[row][2])
            # ax.plot(principal_df[row][0], principal_df[row][1], principal_df[row][2], ".r")
        if pred == 1:  # Second cluster
            listXb.append(cleared_dataset[row][0])
            listYb.append(cleared_dataset[row][1])
            listZb.append(cleared_dataset[row][2])
            # ax.plot(principal_df[row][0], principal_df[row][1], principal_df[row][2], ".b")

        if pred == 2:  # Second cluster
            listXy.append(cleared_dataset[row][0])
            listYy.append(cleared_dataset[row][1])
            listZy.append(cleared_dataset[row][2])
            # ax.plot(principal_df[row][0], principal_df[row][1], principal_df[row][2], ".y")

        if pred == 3:  # Second cluster
            listXg.append(cleared_dataset[row][0])
            listYg.append(cleared_dataset[row][1])
            listZg.append(cleared_dataset[row][2])
            # ax.plot(principal_df[row][0], principal_df[row][1], principal_df[row][2], ".g")

    print(c)
    ax.scatter(listXr, listYr, listZr, c='r', marker='o')
    ax.scatter(listXb, listYb, listZb, c='b', marker='o')
    ax.scatter(listXy, listYy, listZy, c='y', marker='o')
    ax.scatter(listXg, listYg, listZg, c='g', marker='o')


if __name__ == "__main__":
    # columns_to_use = ['carbohydrates_100g', 'proteins_100g', 'salt_100g']
    columns_to_use = ['serving_quantity', 'energy_100g', 'saturated-fat_100g']
    # columns_to_use = ['serving_quantity', 'energy_100g', 'fat_100g', 'saturated-fat_100g']
    data = load_data(columns_to_use)
    plot_kmeans_3d(data)
    plt.show()
