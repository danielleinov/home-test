FROM python:3-alpine

RUN apk add --no-cache python3-dev libffi-dev build-base openssl-dev

COPY app/requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

# Expose the Flask port
EXPOSE 5000

CMD [ "python3", "manage.py", "runserver" , "--host" ,"0.0.0.0"]