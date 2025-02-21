FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y netcat && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "while ! nc -z db 5432; do sleep 1; done && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
