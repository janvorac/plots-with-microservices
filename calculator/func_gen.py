from concurrent import futures
import numpy as np
import grpc

from func_gen_pb2 import (
    CalcRequest,
    CalcResponse,
)
import func_gen_pb2_grpc


NUMPOINTS = 500


class CalcService(
    func_gen_pb2_grpc.CalcServiceServicer
):
    def Calc(self, request: CalcRequest, context):
        x = np.linspace(request.x_start, request.x_end, NUMPOINTS)
        y = ( request.constant + 
            x * request.linear_coefficient +
            x ** 2 * request.quadratic_coefficient +
            x ** 3 * request.cubic_coefficient
        )
        return CalcResponse(x=x, y=y)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    func_gen_pb2_grpc.add_CalcServiceServicer_to_server(
        CalcService(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
