FROM python:3.8

WORKDIR /app

COPY response_time_exporter.py settings.py /app/

RUN pip install prometheus_client requests

CMD ["python", "response_time_exporter.py"]

