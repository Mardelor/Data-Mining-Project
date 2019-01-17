from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
from tools import load_data


def plot_kmeans_2d(cleared_dataset, columns_to_use):
    # Do the KMeans
    nb_clusters = 4
    random_state = 50
    kmeans = KMeans(n_clusters=nb_clusters, random_state=random_state).fit(cleared_dataset)
    print("Centres: ", kmeans.cluster_centers_)

    # The graph
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.autoscale(enable=True, axis='both', tight=None)
    ax.set_title('KMeans')
    ax.set_xlabel(columns_to_use[0])
    ax.set_ylabel(columns_to_use[1])

    # Plot the clusters obtained
    c = 0
    cleared_dataset = np.array(cleared_dataset)
    listXr, listYr, listXy, listYy = [], [], [], []
    listXg, listYg, listXb, listYb = [], [], [], []

    for row in range(len(cleared_dataset)):
        data = [cleared_dataset[row][x] for x in range(cleared_dataset.shape[1])]
        data = np.array(data)
        data = data.reshape(1, -1)
        pred = kmeans.predict(data)  # For each product, we determine in which cluster it is
        if pred == 0:  # First cluster
            c += 1
            listXr.append(data[0][0])
            listYr.append(data[0][1])
        if pred == 1:  # Second cluster
            listXy.append(data[0][0])
            listYy.append(data[0][1])
        if pred == 2:  # Second cluster
            listXg.append(data[0][0])
            listYg.append(data[0][1])
        if pred == 3:  # Second cluster
            listXb.append(data[0][0])
            listYb.append(data[0][1])
    print(c)
    plt.plot(listXr, listYr, ".r")
    plt.plot(listXy, listYy, ".y")
    plt.plot(listXg, listYg, ".g")
    plt.plot(listXb, listYb, ".b")


if __name__ == "__main__":
    columns_to_use = ['carbohydrates_100g', 'proteins_100g']
    # columns_to_use = ['energy_100g', 'carbohydrates_100g']
    # columns_to_use = ['carbohydrates_100g', 'proteins_100g', 'sugars_100g', 'monounsaturated-fat_100g',
    #                   'polyunsaturated-fat_100g', 'fat_100g', 'saturated-fat_100g']
    # columns_to_use = ['sodium_100g', 'salt_100g']
    cleared_dataset = load_data(columns_to_use)
    plot_kmeans_2d(cleared_dataset, columns_to_use)
    plt.show()
