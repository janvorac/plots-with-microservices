import os

from flask import Flask, render_template
import grpc

from func_gen_pb2 import CalcRequest
from func_gen_pb2_grpc import CalcServiceStub


app = Flask(__name__)

calc_host = os.getenv("CALC_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{calc_host}:50051"
)

calc_client = CalcServiceStub(recommendations_channel)


@app.route("/")
def render_homepage():
    calc_request = CalcRequest(
        x_start=-5,
        x_end=5,
        constant=0,
        linear_coefficient=1,
        quadratic_coefficient=0.5,
        cubic_coefficient=0.1
    )
    recommendations_response = calc_client.Calc(
        calc_request
    )
    return render_template(
        "home.html",
        x=recommendations_response.x,
        y=recommendations_response.y
    )