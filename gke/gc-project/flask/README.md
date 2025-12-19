
gcloud iam service-accounts add-iam-policy-binding naokit-sa@datadog-tse-sandbox.iam.gserviceaccount.com \
          --member="user:naoki.tsukuda@datadoghq.com" \
          --role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding datadog-tse-sandbox \
     --member=serviceAccount:622512481889-compute@developer.gserviceaccount.com \
     --role=roles/run.builder

## How to update app
1. gcloud run deploy flask-naokit --source .
