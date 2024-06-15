gcloud builds submit --tag gcr.io/forecast-bawang-merah-426507/index
gcloud run deploy --image gcr.io/forecast-bawang-merah-426507/index --platform managed