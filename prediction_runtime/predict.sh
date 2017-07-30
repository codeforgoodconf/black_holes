UNLABELED=$1
java -cp /wekainstall/weka/weka.jar weka.Run -no-scan weka.classifiers.functions.MultilayerPerceptron -classifications "weka.classifiers.evaluation.output.prediction.CSV" -l multilayerperceptronsmall.model -T $1 -c 1 > predictions.csv
cat predictions.csv