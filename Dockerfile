FROM ubuntu:bionic
LABEL maintenier="duvan.ballen@gmail.com"
RUN apt-get update -y && \ 
    apt-get upgrade -y && \
    apt-get install -y python3-dev python3-pip build-essential netcat curl binutils
ADD . /app
RUN pip3 install -r /app/requirements.txt
WORKDIR /app
CMD cd /app
CMD ["run.py"]