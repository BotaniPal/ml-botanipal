import requests
import time

# url = 'https://get-prediction-bd2k3j3bjq-as.a.run.app'
url = 'http://localhost:5000'
data = {
    "future_date": "2024-06-18",
}

max_retries = 5
backoff_factor = 1

for attempt in range(max_retries):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON.")
        break
    elif response.status_code == 503:
        print(f"Attempt {attempt + 1}: Service Unavailable. Retrying in {backoff_factor} seconds...")
        time.sleep(backoff_factor)
        backoff_factor *= 2
    else:
        print(f"Failed with status code: {response.status_code}")
        print("Response Text:", response.text)
        break
else:
    print("Max retries reached. Service is unavailable.")
