import requests

resp = requests.post("https://getprediction-5fhrsocmfa-et.a.run.app", files={'file': open('apple.jpg', 'rb')})

print(resp.json())