FROM python:3.9.2-slim

RUN "mkdir app"

WORKDIR app/

COPY . .

EXPOSE 8008

CMD ["flask", "run"]
