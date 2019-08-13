FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY wait-for-it.sh /usr/local/bin/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
