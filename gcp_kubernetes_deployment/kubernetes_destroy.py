import subprocess
from subprocess import check_output
import sys
import os
import argparse

def main():
 parser = argparse.ArgumentParser(description='MavenCode Kubernetes cluster destruction')
 parser.add_argument('--name', type=str, help='Kubernetes cluster name', required=True)
 parser.add_argument('--zone', type=str, help='Compute zone (e.g. us-central1-a) for the cluster. Overrides the default compute/zone property value for this command invocation.', required=True)
 parser.add_argument('--topic', type=str, help='pubsub topic needs to be specified', required=True)
 parser.add_argument('--subscription', type=str, help='pubsub subscription needs to be scpecified', required=True)

 args = parser.parse_args()
 name = args.name
 zone = args.zone
 topic = args.topic
 subscription = args.subscription

 check_cluster_exists = "gcloud container clusters list | grep "+ name 
 cluster = check_output([check_cluster_exists], shell=True) 
 if cluster == "":
  print 'There is no kubernetes cluster with this name \n Please check the name of the cluster'
 else:
  print 'Destroying kubernetes cluster ...' + name
  delete_cluster = "gcloud container clusters delete " + name
  subprocess.call([delete_cluster], shell=True)
  print 'Kubernetes cluster '+ name + ' is destroyed'
 check_topic_exists = "gcloud pubsub topics list | grep " + topic
 topic =  check_output([check_cluster_exists], shell=True)
 if topic == "":
  print 'There is no pubsub topic with this name \n Please check the name of the topic'
 else:
  print 'Destroying pubsub topic ...'
  delete_pubsub_topic = "gcloud pubsub topics delete " + topic
  subprocess.call([delete_pubsub_topic], shell=True)
  print 'pubsub topic '+ topic + ' is destroyed'
 check_subscription_exists = "gcloud pubsub subscriptions list | grep " + subscription
 topic =  check_output([check_subscription_exists], shell=True)
 if topic == "":
  print 'There is no pubsub topic with this name \n Please check the name of the topic'
 else:
  print 'Destroying pubsub subscription ...'
  delete_pubsub_subscription = "gcloud alpha pubsub subscriptions delete " + subscription
  subprocess.call([delete_pubsub_subscription], shell=True)
  print 'pubsub subscription '+ subscription + ' is destroyed'

if __name__ == "__main__":
 main()
