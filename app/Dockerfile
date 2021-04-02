FROM python:3.9.2-buster

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
