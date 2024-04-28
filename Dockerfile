FROM python:3.11-slim-bookworm
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "run", "bin/server.py"]
