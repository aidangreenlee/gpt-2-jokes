FROM tensorflow/tensorflow:latest-py3

WORKDIR /tf/GPT2/

COPY jokes.py jokes.py
COPY checkpoint_run1.tar checkpoint_run1.tar

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN pip3 install gpt-2-simple
RUN pip3 install tensorflow==1.15
RUN tar -xvf checkpoint_run1.tar
