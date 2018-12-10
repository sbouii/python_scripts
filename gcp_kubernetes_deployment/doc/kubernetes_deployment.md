#### Deploy kubernetes cluster: Goto Section on DockerContainer Deploy

#```
# sudo python kubernetes_deployment.py --name CLUSTER-NAME --zone ZONE-NAME   
#```
#- you can add other arguments for the configuration of the kubernetes cluster.
#
#  to see the other configuration options type:
   
#```
#  python kubernetes_deployment.py --help
#```
#- what the script will do is:
#
#   - Set up the kubernetes cluster.
#   - Deploy jenkins on the kubernetes cluster using Helm.


***SETUP STEPS***
1. set up the cluster
2. build the jenkins image and push the gcr
3. install the jenkins helm
*****************


#Runnning Inside the Docker Container

0. Docker Build: `docker build -t smartdeployai/kubernetes_deploy -f Dockerfile .` <= if successful docker push

1. Docker Run: `docker run -it smartdeployai/kubernetes_deploy /bin/bash`

2. Run `python kubernetes_deployment.py --name smartops-kubernetes --zone us-central1-a --project_id smartdeployai --pubsub_notification projects/smartdeployai/topics/smartdeploy-pubsub-deployment-topic --scopes "https://www.googleapis.com/auth/projecthosting,storage-rw" --addons HttpLoadBalancing,HorizontalPodAutoscaling,KubernetesDashboard,Istio --go_live`

3. Takes a while for step 2. to get done and after that you can  check to se the container is deployed correctly

-> `gcloud container clusters list`

-> `gcloud container clusters get-credentials smartops-kubernetes --zone=us-central1-a` this will grab the Kubeconfig and write it to the correct location

-> `kubectl get pods --all-namespaces`




#Helm Install
create our project namespace => `kubectl create namespace smartops`
create jenkins app => `./helm install --name smartops-jenkins helm_deploy/jenkins --namespace smartops --debug` and run `./helm del --purge smartops-jenkins` to delete

JENKINS DEPLOY NOTE =>

```
NOTES:
1. Get your 'admin' user password by running:
  printf $(kubectl get secret --namespace smartops smartops-jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode);echo
2. Get the Jenkins URL to visit by running these commands in the same shell:
  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        You can watch the status of by running 'kubectl get svc --namespace smartops -w smartops-jenkins'
  export SERVICE_IP=$(kubectl get svc --namespace smartops smartops-jenkins --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")
  echo http://$SERVICE_IP:8080/login

3. Login with the password from step 1 and the username: admin

For more information on running Jenkins on Kubernetes, visit:
https://cloud.google.com/solutions/jenkins-on-container-engine
```


#configuring docker registry on gcp

make sure that account is linked to billing account

example
```gcloud alpha billing accounts projects link PROJECT-ID --billing-account=ACCOUNT-ID```

if you need to get the accountId =>
```gcloud alpha billing accounts list```

0. Enable services: `gcloud services enable containerregistry.googleapis.com`

1. RUN `gcloud auth configure-docker` :Response =>

```
{
  "credHelpers": {
    "gcr.io": "gcloud", 
    "us.gcr.io": "gcloud", 
    "eu.gcr.io": "gcloud", 
    "asia.gcr.io": "gcloud", 
    "staging-k8s.gcr.io": "gcloud", 
    "marketplace.gcr.io": "gcloud"
  }
}
```

2. Combine hostname with image name [HOSTNAME]/[PROJECT-ID]/[IMAGE] =>

i.e gcr.io/smartdeployai/kubernetes_deployer

docker tag [SOURCE_IMAGE] [HOSTNAME]/[PROJECT-ID]/[IMAGE]

i.e docker tag smartdeployai/kubernetes_deployer gcr.io/smartdeployai/kubernetes_deployer

then docker push [HOSTNAME]/[PROJECT-ID]/[IMAGE] 

i.e docker push gcr.io/smartdeployai/kubernetes_deployer:latest

check to see if the image was successfully pushed `gcloud container images list-tags [HOSTNAME]/[PROJECT-ID]/[IMAGE]`

gcloud container images list-tags gcr.io/smartdeployai/kubernetes_deployer:latest

To pull image => docker pull [HOSTNAME]/[PROJECT-ID]/[IMAGE]:[TAG]

`docker pull gcr.io/smartdeployai/kubernetes_deployer:latest`


To delete image => gcloud container images delete [HOSTNAME]/[PROJECT-ID]/[IMAGE]:[TAG]

`gcloud container images delete gcr.io/smartdeployai/kubernetes_deployer:latest`

