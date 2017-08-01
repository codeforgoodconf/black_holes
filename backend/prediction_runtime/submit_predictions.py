import requests
data = {
    "predictions": {
        "spec-1305-52757-0269": 0.983,
        "spec-1306-52996-0005": 0.983,
        "spec-1306-52996-0230": 0.983,
    }
}
result = requests.post("http://127.0.0.1:5000/predict", json=data)
print(result.text)