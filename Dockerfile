# pull official base image
FROM python:3.11-slim-bookworm

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

COPY ./requirements.txt /app

# install dependencies
RUN pip install --upgrade pip setuptools && pip install -r requirements.txt

# Show all installed modules
COPY . .
EXPOSE 8080

# run entrypoint.sh
CMD ["python", "bin/server.py"]
