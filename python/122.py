def knuth(items):
    for i in range(len(items)):
        j=randrange(i, len(items))
        items[i], items[j] = items[j], items[i]