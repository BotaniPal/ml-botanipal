import requests

resp = requests.post("https://getprediction-akgztv2v4a-et.a.run.app/", files={'file': open('C:/Users/Ghifary/OneDrive/Documents/Kuliah/BANGKIT/Deploy/0d8d5b80-962d-4381-8d3b-9eca3f2f1bb0___FREC_Scab 3449_new30degFlipLR.JPG', 'rb')})

print(resp.json())