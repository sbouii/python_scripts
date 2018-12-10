FROM google/cloud-sdk:latest
RUN apt-get update && \
    apt-get install -y software-properties-common sshpass openssh-client \
    git libffi6 libffi-dev libssl-dev python-dev python3-dev python-pip build-essential && \
    pip install --upgrade pip && \
    pip install pyOpenSSL==16.2.0 && \
    pip install ansible && \
    pip install google-cloud-pubsub && \
    rm -rf /var/lib/apt/lists/*
ENV INSTANCE-NAME
ENV DEPLOYMENT-NAME
ENV TEMPLATE
ENV ZONE
ENV MACHINE-TYPE
ENV DEVICE-NAME
ENV TYPE
ENV BOOT
ENV AUTODELETE
ENV IMAGE-PROJECT
ENV IMAGE-FAMILY
ENV NETWORK-NAME
ENV NETWORK-TYPE
ADD . /vm-deployment
WORKDIR /vm-deployment
ENTRYPOINT python boostrap_vm.py --instance_name=${INSTANCE-NAME} --deployment_name=${DEPLOYMENT-NAME} --template=${TEMPLATE} --zone=${ZONE} --machineType=${MACHINE-TYPE} --deviceName=${DEVICE-NAME} --type=${TYPE} --boot=${BOOT} --autoDelete=${AUTODELETE} --imageProject=${IMAGE-PROJECT} --imageFamily=${IMAGE-FAMILY} --networkName=${NETWORK-NAME} --networkType=${NETWORK-TYPE}  

