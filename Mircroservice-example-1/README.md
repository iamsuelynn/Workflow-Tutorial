## Running Docker file on Cloud Run 
gcloud config set run/region asia-southeast1

gcloud builds submit --tag gcr.io/sue-gcp-learning-env/microservices_example_1

gcloud run deploy --image gcr.io/sue-gcp-learning-env/microservices_example_1 --platform managed
