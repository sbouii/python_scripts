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
ADD . /postgres
WORKDIR /postgres
ENTRYPOINT python bootstrap.py --instance_name=${INSTANCE-NAME}
