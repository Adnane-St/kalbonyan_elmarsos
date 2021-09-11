# Here we will use hash table unique key in order to filter a list


def filter(list):
    fil = dict()
    for itm in list:
        fil[itm] = 0
    return set(fil.keys())

print(filter(['orng','orng','orange','apple']))