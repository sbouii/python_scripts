FROM google/cloud-sdk:latest
RUN apt-get update && \
    apt-get install -y software-properties-common sshpass openssh-client \
    git libffi6 libffi-dev libssl-dev python-dev python3-dev python-pip build-essential && \
    pip install --upgrade pip && \
    pip install pyOpenSSL==16.2.0 && \
    pip install ansible && \
    pip install google-cloud-pubsub && \
    rm -rf /var/lib/apt/lists/*
ENV NAME
ENV ZONE
ENV MASTER-TYPE
ENV WORKER-TYPE
ENV MASTER-NUMBER
ENV WORKER-NUMBER
ENV JOB-LANGUAGE
ENV STORAGE-BUCKET
ENV JOB-PYTHON
ADD . /dataproc
WORKDIR /dataproc
ENTRYPOINT python dataproc_script.py --name=${NAME} --zone=${ZONE} --master_machine_type=${MASTER-TYPE} --worker_machine_type=${WORKER-TYPE} --masters_number=${MASTER-NUMBER} --workers_number=${WORKER-NUMBER} --job_language=${JOB-LANGUAGE} --storage_bucket=${STORAGE-BUCKET} --job_python=${JOB-PYTHON}
