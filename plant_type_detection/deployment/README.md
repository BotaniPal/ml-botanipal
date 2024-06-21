# How to Deploy Plant Disease Model
Link of deployment: https://getprediction-5fhrsocmfa-et.a.run.app

### 1. Write App (Flask, TensorFlow)
- The code to build, train, and save the model is in the `test` folder.
- Implement the app in `main.py`
- 
### 2. Setup Google Cloud 
- Create new project
- Activate Cloud Run API and Cloud Build API
- 
### 3. Install and init Google Cloud SDK
- https://cloud.google.com/sdk/docs/install

### 4. Dockerfile, requirements.txt, .dockerignore
- https://cloud.google.com/run/docs/quickstarts/build-and-deploy#containerizing

### 5. Cloud build & deploy
```
gcloud builds submit --tag gcr.io/deploy-plant-type-detection/index
gcloud run deploy --image gcr.io/deploy-plant-type-detection/index --platform managed
```

### 6. To test the model, you can use test.py file
