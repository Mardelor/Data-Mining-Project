import pandas as pd
from tools import columns, clean_cells, data


def test_2():
    nb_in_group = 2
    list_ok = []

    for i in range(len(columns) - nb_in_group + 1):
        for j in range(i+1, len(columns) - nb_in_group + 1):
            columns_to_use = [columns[i], columns[j]]
            print(columns_to_use)

            dataset = pd.read_csv(data, encoding='latin_1', engine='python',
                                  usecols=['code', 'product_name'] + columns_to_use,
                                  nrows=100,  # The number of rows we study
                                  sep='[\t\r]')
            # Clean data
            cleared_dataset, dropped = clean_cells(dataset)

            if float(dropped) < 70.0:
                list_ok.append(columns_to_use + [dropped])

    return list_ok


def test_3():
    nb_in_group = 3
    list_ok = []

    for i in range(len(columns) - nb_in_group + 1):
        for j in range(i+1, len(columns) - nb_in_group + 1):
            for k in range(j+1, len(columns) - nb_in_group + 1):

                columns_to_use = [columns[i], columns[j], columns[k]]
                print(columns_to_use)

                dataset = pd.read_csv(data, encoding='latin_1', engine='python',
                                      usecols=['code', 'product_name'] + columns_to_use,
                                      nrows=100,  # The number of rows we study
                                      sep='[\t\r]')
                # Clean data
                cleared_dataset, dropped = clean_cells(dataset)

                if float(dropped) < 70.0:
                    list_ok.append(columns_to_use + [dropped])

    return list_ok


def test_4():
    nb_in_group = 4
    list_ok = []

    for i in range(len(columns) - nb_in_group + 1):
        for j in range(i+1, len(columns) - nb_in_group + 1):
            for k in range(j+1, len(columns) - nb_in_group + 1):
                for l in range(k+1, len(columns) - nb_in_group + 1):

                    columns_to_use = [columns[i], columns[j], columns[k], columns[l]]
                    print(columns_to_use)

                    dataset = pd.read_csv(data, encoding='latin_1', engine='python',
                                          usecols=['code', 'product_name'] + columns_to_use,
                                          nrows=100,  # The number of rows we study
                                          sep='[\t\r]')
                    # Clean data
                    cleared_dataset, dropped = clean_cells(dataset)

                    if float(dropped) < 70.0:
                        list_ok.append(columns_to_use + [dropped])

    return list_ok


def test_5():
    nb_in_group = 5
    list_ok = []

    for i in range(len(columns) - nb_in_group + 1):
        for j in range(i+1, len(columns) - nb_in_group + 1):
            for k in range(j+1, len(columns) - nb_in_group + 1):
                for l in range(k+1, len(columns) - nb_in_group + 1):
                    for m in range(l+1, len(columns) - nb_in_group + 1):

                        columns_to_use = [columns[i], columns[j], columns[k], columns[l], columns[m]]
                        print(columns_to_use)

                        dataset = pd.read_csv(data, encoding='latin_1', engine='python',
                                              usecols=['code', 'product_name'] + columns_to_use,
                                              nrows=100,  # The number of rows we study
                                              sep='[\t\r]')
                        # Clean data
                        cleared_dataset, dropped = clean_cells(dataset)

                        if float(dropped) < 70.0:
                            list_ok.append(columns_to_use)

    return list_ok


if __name__ == "__main__":
    list_ok = test_2()
    print("Enough data for: ", list_ok)
    # list_ok = test_3()
    # print("Enough data for: ", list_ok)
    # list_ok = test_4()
    # print("Enough data for: ", list_ok)
    # list_ok = test_5()
    # print("Enough data for: ", list_ok)
