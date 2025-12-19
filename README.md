## Summary
* Simple sandbox to be deployed to GKE Autopilot.
* Components included: 
** Datadog Agent
** Web server (Flask)

## Prerequisites
1. Install the Google Cloud CLI following [https://docs.cloud.google.com/sdk/docs/install-sdk] if you haven't.
2. Replace the following on `./gke/autopilot/datadog-values.yaml` with your API key and APP key.
* `<DATADOG_API_KEY>`
* `<DATADOG_APP_KEY>`

## Usage
* See `./gke/README.md` for details.
