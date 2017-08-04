import math

def run(data, labels, n):

    rows = len(data)
    cols = len(data[0])

    # Compute means

    m0 = []
    m1 = []
    for j in range(0, cols, 1):
        m0.append(1)
        m1.append(1)

    for i in range(0, rows, 1):
        if labels.get(i) is not None and labels[i] == 0:
            for j in range(0, cols, 1):
                m0[j] += data[i][j]
        if labels.get(i) is not None and labels[i] == 1:
            for j in range(0, cols, 1):
                m1[j] += data[i][j]

    for j in range(0, cols, 1):
        m0[j] /= n[0]
        m1[j] /= n[1]

    # print(m0)
    # print(m1)


    # compute standard deviations

    s0 = [0.0]*cols
    s1 = [0.0]*cols

    for i in range(0, rows, 1):
        if labels.get(i) is not None and labels[i] == 0:
            for j in range(0, cols, 1):
                s0[j] += (data[i][j] - m0[j]) ** 2
        if labels.get(i) is not None and labels[i] == 1:
            for j in range(0, cols, 1):
                s1[j] += (data[i][j] - m1[j]) ** 2

    for j in range(0, cols, 1):
        s0[j] = math.sqrt(s0[j] / n[0])
        s1[j] = math.sqrt(s1[j] / n[1])

    # print(s0)
    # print(s1)

    # Classify unlabeled points

    for i in range(0, rows, 1):
        if labels.get(i) is None:
            d0 = 0
            d1 = 0
            for j in range(0, cols, 1):
                if s0[j] == 0.0 or s1[j] == 0.0:  #KLUGE
                    continue
                d0 += ((data[i][j] - m0[j]) / s0[j]) ** 2
                d1 += ((data[i][j] - m1[j]) / s1[j]) ** 2
            if d0 < d1:
                # print("0 ", i)
                labels[i] = 0
            else:
                # print("1 ", i)
                labels[i] = 1
