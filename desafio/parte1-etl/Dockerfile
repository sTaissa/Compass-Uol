FROM python:3

WORKDIR /app

COPY . .

RUN pip install boto3

CMD ["etl.py"]

ENTRYPOINT ["python3"]