import math


def run(data, labels, n):

    k = 1

    rows = len(data)
    cols = len(data[0])

    # Classify unlabeled points
    for i in range(rows):
        if labels.get(i) is None:
            d = []
            for i2 in range(rows):
                if labels.get(i2) is not None:
                    d.append((labels[i2], distancesquared(data[i], data[i2])))

            d = sorted(d, key=lambda ds: ds[1])

            n0 = 0
            n1 = 0
            for i2 in range(min(k, len(d))):
                if d[i2][0] == 0:
                    n0 += 1
                else:
                    n1 += 1

            if n0 > n1:
                labels[i] = 0
            else:
                labels[i] = 1

def distancesquared(p0, p1):
    d = 0
    for j in range(len(p0)):
        d += (p0[j] - p1[j]) ** 2
    return d
