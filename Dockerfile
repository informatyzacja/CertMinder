FROM ubuntu:22.04

RUN apt-get update && apt-get install git python3 python3-pip -y && apt-get clean

RUN pip3 install git+https://github.com/informatyzacja-sspwr-projekty/CertMinder.git

COPY certminder.yml /certminder.yml

CMD certminder -s -c
