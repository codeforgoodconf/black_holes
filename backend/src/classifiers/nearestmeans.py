

def run(data, labels, n):

    rows = len(data)
    cols = len(data[0])

    # Compute means

    m0 = []
    m1 = []
    for j in range(cols):
        m0.append(0)
        m1.append(0)

    for i in range(0, rows, 1):
        if labels.get(i) is not None and labels[i] == 0:
            for j in range(0, cols, 1):
                m0[j] += data[i][j]
        if labels.get(i) is not None and labels[i] == 1:
            for j in range(0, cols, 1):
                m1[j] += data[i][j]

    for j in range(cols):
        m0[j] /= n[0]
        m1[j] /= n[1]

    # print(m0)
    # print(m1)

    # Classify unlabeled points
    for i in range(rows):
        if labels.get(i) is None:
            d0 = 0
            d1 = 0
            for j in range(cols):
                d0 += (m0[j] - data[i][j]) ** 2
                d1 += (m1[j] - data[i][j]) ** 2
            if d0 < d1:
                labels[i] = 0
            else:
                labels[i] = 1
