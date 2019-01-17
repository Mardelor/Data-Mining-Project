import pandas as pd
import numpy as np
from analyse_ACP_2D import plot_pca, plt
from tools import print_columns_names, clean_cells, delete_columns, data


def countries(columns_to_use):
    # Load data
    dataset = pd.read_csv(data, encoding='utf-8', engine='python',
                                usecols=['code', 'product_name'] + columns_to_use,
                                nrows=10000,  # The number of rows we study
                                sep='[\t\r]')
    print_columns_names(dataset)

    # Clean data
    cleared_dataset, dropped = clean_cells(dataset)
    cleared_dataset = delete_columns(cleared_dataset, ['code', 'product_name'])
    nb_col = 1

    cleared_dataset = np.array(cleared_dataset)
    list_countries = []
    #
    # for i in range(cleared_dataset.shape[0]):
    #     elts = cleared_dataset[i][nb_col-1].split(",")
    #     for elt in elts:
    #         if elt not in list_countries:
    #             list_countries.append(elt)
    #
    # print(list_countries)

    for i in range(cleared_dataset.shape[0]):
        elt = cleared_dataset[i][nb_col-1]
        if elt not in list_countries:
            list_countries.append(elt)

    print(list_countries)

    for i in range(cleared_dataset.shape[0]):
            cleared_dataset[i][nb_col-1] = list_countries.index(cleared_dataset[i][nb_col-1])

    cleared_dataset = pd.DataFrame(data=cleared_dataset)
    clean_cells(cleared_dataset)

    return cleared_dataset


if __name__ == "__main__":
    columns_to_use = ['countries_tags', 'carbohydrates_100g']
    cleared_dataset = countries(columns_to_use)
    plot_pca(cleared_dataset)
    plt.show()
