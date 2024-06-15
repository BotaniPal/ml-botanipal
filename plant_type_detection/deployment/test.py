import requests

url = "https://deploy-plant-type-detection-5fhrsocmfa-et.a.run.app"
data = {
    "file_url": "https://storage.googleapis.com/backend-nodejs-tes.appspot.com/predictions/iepEjK1YtodBfCD2ZPYC8MDaWUR2_1718348727413.jpg"
}
response = requests.post(url, json=data)

print(response.json())