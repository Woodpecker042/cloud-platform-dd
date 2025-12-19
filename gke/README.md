Ref. https://docs.datadoghq.com/containers/kubernetes/distributions/?tab=helm#autopilot

## Connect to GKE cluster
Ref. https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#connecting_to_the_cluster

## One time
* Create Autopilot cluster on GKE
```
gcloud container clusters create-auto naokit-auto-doglib \
    --location=asia-northeast2
```

* [Standard (not Autopilot)]Create cluster on GKE
```
gcloud container clusters create naokit-doglib --num-nodes 1 --zone "asia-northeast2-b" --scopes "cloud-platform"
```

## [Optional, tips] Change kubectl contexts
* List contexts
```
kubectl config get-contexts
```
* Set context
```
kubectl config set context <context_name>
```
* Get current context
```
kubectl config current-context
```