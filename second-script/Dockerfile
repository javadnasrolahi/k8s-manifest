FROM python:3.8-slim-buster 
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y curl
COPY . .
ENTRYPOINT ["python", "-u"]
# CMD ["sleep.py"]
CMD ["convert-epoch.py"]