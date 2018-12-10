FROM google/cloud-sdk:latest

#docker build -t smartdeployai/kubernetes_deploy -f Dockerfile .

RUN apt-get update && \
    apt-get install -y software-properties-common sshpass openssh-client nano \
    git libffi6 libffi-dev libssl-dev python-dev python3-dev python-pip build-essential && \
    pip install --upgrade pip && \
    pip install pyOpenSSL==16.2.0 && \
    pip install jinja2 && \
    pip install ansible && \
    pip install google-cloud-pubsub && \
    rm -rf /var/lib/apt/lists/*
ENV NAME
ENV ZONE
ENV PROJECT-ID
ENV PUBSUB-NOTIFICATION
ADD . /kubernetes
ENTRYPOINT python /kubernetes/kubernetes_deployment.py --name ${NAME} --zone ${ZONE} --project_id ${PROJECT-ID} --pubsubNotification ${PUBSUB-NOTIFICATION}
