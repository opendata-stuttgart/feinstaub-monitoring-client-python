FROM python:3.5-slim

USER root
# try to fix DNS issues with googles DNS (still failing)
# RUN 'echo "nameserver 8.8.8.8" >> /etc/resolv.conf'
# file does not exist in image
RUN pip install --upgrade pip

ADD . /opt/code
WORKDIR /opt/code

RUN pip install -r /opt/code/requirements.txt

#COPY config.py /opt/code
CMD python monitor.py
CMD python monitor.py --push
