FROM python:3.7-alpine

WORKDIR /srb/app

COPY . .

RUN pip install --no-cache-dir pipenv==2018.11.26 &&\
    pipenv install --system --deploy

ENV OUTDIR .
ENV WORKERS 4
ENV PORT 9000
EXPOSE $PORT

CMD gunicorn -c gunicorn.conf.py "app:app"
