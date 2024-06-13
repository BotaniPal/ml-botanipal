import requests

# Daftar nama file gambar yang ingin diuji
file_names = ['apple.jpg', 'soybeans.jpg', 'cauliflower.jpg']

# URL endpoint
url = "https://getprediction-5fhrsocmfa-et.a.run.app"

# Loop melalui setiap file
for file_name in file_names:
    with open(file_name, 'rb') as file:
        # Kirim request POST
        resp = requests.post(url, files={'file': file})
        
        # Cek status kode
        if resp.status_code == 200:
            try:
                # Coba parsing JSON
                print(f"Response untuk {file_name}: {resp.json()}")
            except ValueError:
                # Tangani error jika response bukan JSON
                print(f"Response untuk {file_name} tidak berisi JSON.")
                print("Isi Response:", resp.text)
        else:
            print(f"Error: Status code {resp.status_code} untuk {file_name}")
            print("Isi Response:", resp.text)