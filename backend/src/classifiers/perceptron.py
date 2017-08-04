import math
import random


def run(data, labels, n):

    rows = len(data)
    for i in range(rows):
        data[i].append(1)

    cols = len(data[0])
    w0_range = 0.001
    eta = 0.001
    threshold = 0.0001

    for i in range(rows):
        if labels.get(i) is not None:
            if labels[i] == 0:
                labels[i] = -1

    # initialize w
    w = [0]*cols
    for j in range(cols):
        w[j] = 2*w0_range*random.random() - w0_range

    last_error = 1000
    error = 100
    while last_error - error > threshold:

        # compute delta f
        df = [0]*cols
        for i in range(rows):
            if labels.get(i) is not None:
                dp = dot(w, data[i])
                for j in range(cols):
                    df[j] += (labels.get(i)-dp)*data[i][j]

        # update w
        for j in range(cols):
            w[j] += eta*df[j]

        # compute error
        last_error = error
        error = 0
        for i in range(rows):
            if labels.get(i) is not None:
                error += (labels.get(i) - dot(w, data[i]))**2

        # print("error = ", error)

    # print("w = ", w)
    # print("||w|| = ", magnitude(w))

    # prediction
    for i in range(rows):
        if labels.get(i) is None:
            dp = dot(w, data[i])
            if dp < 0:
                # print("0 ", i)
                labels[i] = 0
            else:
                # print("1 ", i)
                labels[i] = 1


def magnitude(a):
    r = 0
    for i in range(len(a)):
        r += a[i]**2
    return math.sqrt(r)


def dot(a, b):
    r = 0
    for i in range(len(a)):
        r += a[i] * b[i]
    return r
