FROM python:3.12-alpine

WORKDIR /app

RUN pip install --no-cache-dir watchdog==6.0.0

COPY src/main.py .

CMD ["python", "-u", "main.py"]
