FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/www/app
WORKDIR /var/www/app
ADD requirements.txt /var/www/app/
RUN pip install -r requirements.txt
ADD . /var/www/app/