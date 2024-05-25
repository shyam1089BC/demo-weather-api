FROM python:alpine3.7

RUN apk add --update --no-cache g++=6.4.0-r5 \
 gcc=6.4.0-r5 \
 build-base=0.5-r0 \
 linux-headers=4.4.6-r2

RUN mkdir -p /app

WORKDIR /app

COPY requirements.pip /app/requirements.pip
RUN pip install -r /app/requirements.pip

COPY . .

EXPOSE 8080

CMD ["python", "application.py"]

