def sort_dict(dc):
    return dict((zip(sorted(dc.keys()), sorted(dc.values()))))


sl = {1: 5, 4: 3, 2: 2, 5: 6, 6: 8}
print(sort_dict(sl))
