FROM ubuntu:24.10
ADD challenge.py /
ADD requirements.txt /
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-venv -y
RUN pip3 install -r requirements.txt --break-system-packages
EXPOSE 4321
CMD ["python3", "challenge.py"]
