FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
