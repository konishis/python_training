def sort(sortlist):
    if sortlist == []:
        return sortlist
    else:
        x, xs = sortlist[0], sortlist[1:]
    return sort([a for a in xs if a < x]) + [x] + sort([a for a in xs if a >= x])
