from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib.request

import numpy as np
import tensorflow as tf

def run(data, labels, n):

    training_data = []
    training_indices = []
    test_data = []
    test_indices = []
    for i in range(len(data)):
        if labels.get(i) is None:
            test_data.append(data[i])
            test_indices.append(i)
        else:
            training_data.append(data[i])
            training_indices.append(i)
    training_labels = list(labels.values())


    # Specify that all features have real-value data
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=300)]

    # build 3-layer DNN with 10, 20, 10 units in each layer
    classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units=[10, 20, 10],
                                                n_classes=2)

    # Define the training inputs
    def get_train_inputs():
        x = tf.constant(training_data)
        y = tf.constant(training_labels)
        return x, y

    # Fit model.
    classifier.fit(input_fn=get_train_inputs, steps=2000)

    # bypass Tensorflow's internal validation
    # Define the test inputs
    # def get_test_inputs():
    #    x = tf.constant(unlabeled_data)
    #    y = tf.constant(test_set.target)
    #     return x, y
    # Evaluate accuracy.
    # accuracy_score = classifier.evaluate(input_fn=get_test_inputs, steps=1)["accuracy"]
    # print("\nTest Accuracy: {0:f}\n".format(accuracy_score))



    def new_samples():
        return np.array(test_data, dtype=np.float32)
    predictions = list(classifier.predict(input_fn=new_samples))

    for i in range(len(test_data)):
        index = test_indices[i]
        labels[index] = predictions[i]



