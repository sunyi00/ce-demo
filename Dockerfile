FROM sunyi00/ubuntu-python:latest

RUN apt-get update && apt-get install -y mysql-client libmysqlclient-dev libpq-dev sqlite3 libffi-dev --no-install-recommends && apt-get -y autoclean && apt-get -y clean && rm -rf /var/cache/apt/archives/* && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN apt-get update && apt-get install -y gcc --no-install-recommends && pip install -r pip-req.txt && apt-get -y remove gcc && apt-get -y autoremove && apt-get -y autoclean && apt-get -y clean && rm -rf /var/cache/apt/archives/* && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
