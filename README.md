# ConveyorFlaskProject

Boilerplate Flask Project for Conveyor Technical Interview

## Running Locally

### Linux

To start the Flask Server in development mode, activate the venv and run:

```
$ make venv
(conveyor-flask-app) $ bin/server.py
```

To run with gunicorn:
```
$ gunicorn --workers=2 -b 0.0.0.0:8080 'conveyor.flask_app:create_app()'
```

### PyCharm

On PyCharm, run bin/server.py.

To validate that the server is ready, open:
```
http://127.0.0.1:8080/api/v1/ready
```

To view the Swagger UI page:
```
http://127.0.0.1:8080/api/v1/
```

## AWS Credentials

You will need to configure your AWS Credentials to use the AWS routes. Follow the instructions on https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html.

If you are running on Linux, your AWS credentials should be located on:
```
~/.aws/credentials
```

If you are running on Windows, your AWS credentials should be located on:
```
C:\Users\USERNAME\.aws\credentials
```

## Running Tests

```
make test
```

## Containerizing the Application

First build your Docker image by running:
```
docker build -t conveyor-flask-app .
```

Then run your image as a container:
```
docker run -p 8080:8080 conveyor-flask-app
```

Alternately, you can run:
```
docker compose up
```

To verify that your service is up, you can run the command:
```
docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                    NAMES
de7b8efed531   conveyor-flask   "python bin/server.py"   8 seconds ago   Up 7 seconds   0.0.0.0:8080->8080/tcp   conveyor-flask-1
```

To run an interactive shell in the container, you can run:
```
docker-compose run --rm flask
docker exec -it b6bebda4e3cb /bin/bash
```
