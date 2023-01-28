Following [this tuorial](https://realpython.com/python-microservices-grpc/), I am trying to create a simple plotting app using the microservice architecture. There are some little specialties to run this app:

 1. Every folder represents a separate service, therefore needs its own virtual environment. Hence the multiple `requirements.txt` files.

  2. In each folder, we need the `grpc`-generated files. To get them, run this command, using the respective virtual envorenment for the service
  `python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/func-gen.proto`

  3. To run the whole app, we need to start all its microservices. So far, it's the calculator service (run with `python func_gen.py`) and the flask server used for visualization (run with `FLASK_APP=vis.py flask run`)