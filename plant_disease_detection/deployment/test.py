import requests

url = "https://prediction-opgb34r6nq-et.a.run.app"
data = {
    "file_url": "https://storage.googleapis.com/backend-nodejs-tes.appspot.com/predictions/iepEjK1YtodBfCD2ZPYC8MDaWUR2_1718349218813.jpeg"
}
response = requests.post(url, json=data)

print(response.json())
