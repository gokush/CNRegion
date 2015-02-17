FROM debian
ADD sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install python python-pip -y
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
EXPOSE 8000