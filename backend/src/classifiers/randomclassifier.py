import random


def run(data, labels, n):
    for i in range(len(data)):
        if labels.get(i) is None:
            labels[i] = random.randint(0, 1)
