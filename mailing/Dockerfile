FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt-get update -y && apt-get install -y netcat
COPY requirements.txt .
RUN pip install -r requirements.txt