import random
import nearestmeans
import bayesian
import perceptron
import logicdiscrimination
import randomclassifier
import knearestneighbor



def splitlabels(labels):

    cv_labels = {}
    cv_validation = {}

    for index in labels:
        if random.randint(1, 10) == 1:
            cv_validation[index] = labels[index]
        else:
            cv_labels[index] = labels[index]

    return cv_labels, cv_validation


def resetlabels(cv_labels, cv_validation):
    for index in cv_validation:
        del cv_labels[index]


"""
n_validation = len(labels) / 10
validation = {}
while len(validation) < n_validation:
    index = random.randint(0, len(labels) - 1)
    if labels.get(index) is not None:
        validation[index] = labels[index]
        del labels[index]
"""


def accuracy(cv_labels, cv_validation):
    correct = 0
    incorrect = 0
    for index in cv_validation:
        if cv_validation[index] == cv_labels[index]:
            correct += 1
        else:
            incorrect += 1
    return correct / (correct + incorrect)


def balancederror(cv_labels, cv_validation):
    a = 0
    b = 0
    c = 0
    d = 0
    for index in cv_validation:
        if cv_validation[index] == 0:
            if cv_labels[index] == 0:
                a += 1
            else:
                b += 1
        else:
            if cv_labels[index] == 0:
                c += 1
            else:
                d += 1
    return 0.5 * (b / (a + b) + c / (c + d))


def parse_csv(file_path):
    data = []
    labels = {}
    with open(file_path, 'r') as file:
        header = file.readline()
        i = 0
        for line in file:
            data_row = line.split(',')
            labels[i] = int(data_row[1])
            data_row = data_row[2:]
            data_row = [float(datum) for datum in data_row]
            data.append(data_row)
            i += 1
    return data, labels


def main():

    # percent_train = 0.5
    # percent_test = 1.0 - percent_train

    file_path = 'D:\\data\\blackhole_spectra\\compiled.csv'

    print('loading '+file_path)
    data, labels = parse_csv(file_path)

    n = [0, 0]
    for i, label in labels.items():
        n[label] += 1

    print('samples: ' + str(len(labels)))
    print('negatives: ' + str(n[0]))
    print('positives: ' + str(n[1]))
    print('iteration\talgorithm\taccuracy')

    classifiers = [knearestneighbor, nearestmeans, bayesian, perceptron, randomclassifier]
    n_iterations = 10
    accuracies = [0.0]*len(classifiers)
    for i in range(n_iterations):

        cv_labels, cv_validation = splitlabels(labels)

        for j in range(len(classifiers)):
            classifier = classifiers[j]
            classifier.run(data, cv_labels, n)
            acc = accuracy(cv_labels, cv_validation)
            print(str(i) + '\t'+classifier.__name__+'\t' + str(acc), flush=True)
            accuracies[j] += acc
            resetlabels(cv_labels, cv_validation)

    for i in range(len(classifiers)):
        accuracies[i] /= n_iterations
        accuracies[i] *= 100
        print('average\t'+classifiers[i].__name__+'\t'+str(accuracies[i]))


if __name__ == '__main__':
    main()
