import json
import sys
original_data = sys.argv[1]
predictions_data = sys.argv[2]

specs = []
with open(original_data, 'r') as f:
	for line in f:
		spec = line.strip().split(',')[0]
		if 'spec' in spec:
			specs.append(spec)

predictions = []
with open(predictions_data, 'r') as f:
	for line in f:
		values = line.strip().split(',')
		if len(values) == 4 and 'inst' not in values[0]:
			predictions.append(float(values[2]))
output = {
    "predictions": dict(zip(specs, predictions))
}
print json.dumps(output)