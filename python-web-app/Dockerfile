FROM python:3.10 as builder

RUN pip install numpy

FROM python:3.10-slim as runner

RUN mkdir /usr/src/app
COPY ./my-app /usr/src/app
COPY ./requirements.txt /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV DATABASE_URL=localhost:5432/fake

CMD ["python", "app.py"]
