import math
import random


def run(data, labels, n):

    rows = len(data)

    cols = len(data[0])
    w_range = 0.01
    eta = 0.01
    threshold = 0.00000001

    # initialize w and w0
    w = [0]*cols
    w0 = 2*w_range*random.random() - w_range
    for j in range(cols):
        w[j] = 2*w_range*random.random() - w_range

    last_error = 1000.0
    error = 100.0
    while last_error - error > threshold:

        # compute dw
        dw = [0]*cols
        for j in range(cols):
            for i in range(rows):
                if labels.get(i) is not None:
                    xi = data[i]
                    yi = labels.get(i)
                    dw[j] += (yi-sigmoid(xi, w, w0))*xi[j]
            dw[j] *= eta

        # compute dw0
        dw0 = 0
        for i in range(rows):
            if labels.get(i) is not None:
                xi = data[i]
                yi = labels.get(i)
                dw0 += yi - sigmoid(xi, w, w0)
        dw0 *= eta

        # update w
        for j in range(cols):
            w[j] += dw[j]

        # update w0
        w0 += dw0

        # compute error
        last_error = error
        error = 0
        for i in range(rows):
            if labels.get(i) is not None:
                xi = data[i]
                yi = labels.get(i)
                ea = math.log(sigmoid(xi, w, w0))
                eb = math.log(nexp(xi, w, w0)/(1+nexp(xi, w, w0)))
                error += -yi*ea - (1-yi)*eb

        # print("error =      ", error)
        # print("last error = ", last_error)
        # print("difference = ",last_error-error)
        # print("threshold =  ",threshold)

    # print("w = ", w)
    # print("||w|| = ", magnitude(w))
    # print("w0/||w|| = ", w0/magnitude(w))

    # prediction
    for i in range(rows):
        if labels.get(i) is None:
            dp = dot(w, data[i]) + w0
            if dp < 0:
                # print("0 ", i)
                labels[i] = 0
            else:
                # print("1 ", i)
                labels[i] = 1


def nexp(x, w, w0):
    try: # KLUGE
        return math.exp(-(dot(w, x)+w0))
    except:
        return 0.0


def sigmoid(x, w, w0):
    return 1/(1+nexp(x, w, w0))


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
