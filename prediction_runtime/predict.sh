UNLABELED_FILE=$1
MODEL_FILE=$2
cp $UNLABELED_FILE original.csv
python strip_unclassified.py $UNLABELED_FILE > stripped.csv
java -cp /wekainstall/weka/weka.jar weka.Run -no-scan weka.classifiers.functions.MultilayerPerceptron -classifications "weka.classifiers.evaluation.output.prediction.CSV" -l $MODEL_FILE -T stripped.csv -c 1 > predictions.csv
cat predictions.csv