# Here we will use hashtable to count item in a list


def count(list):
    fil = dict()
    for match in list:
        if match in set(fil.keys()):
            fil[match] += 1
        else:
            fil[match] = 1
    return fil

print(count(['orng','orng','orange','apple','orange','orange','apple']))