python convert_to_json.py original.csv predictions.csv > payload.json
curl -H "Content-Type: application/json" -X POST --data @payload.json http://app:5000/predict