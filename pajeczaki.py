def stp(slowo):
    tree = None
    tab = []
    for i in range(len(slowo)):
        a = slowo[i]
        element = []
        if len(tab) == 0:
            tree = element
        else:
            x = tab.pop()
            x.append(element)
        if a == 'J':
            tab.append(element)
        if a == 'D':
            tab.append(element)
            tab.append(element)
        if a == 'T':
            tab.append(element)
            tab.append(element)
            tab.append(element)
    return depth(tree)


def depth(tab):
    if len(tab) == 0:
        return 1
    else:
        return max([depth(x) for x in tab]) + 1

assert stp("JDJDZJDZZZ") == 7
assert stp("TJJJDZZDZZJZ") == 6
