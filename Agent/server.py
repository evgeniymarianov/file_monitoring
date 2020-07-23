import grpc
from concurrent import futures
import time

# import the generated classes
import sender_pb2
import sender_pb2_grpc

# import the original sender.py
import sender

# create a class to define the server functions
# derived from sender_pb2_grpc.SenderServicer
class SenderServicer(sender_pb2_grpc.SenderServicer):

    # sender.send is exposed here
    # the request and response are of the data types
    # generated as sender_pb2.Message
    def Send(self, request, context):
        response = sender_pb2.Message()
        response.value = sender.send(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_SenderServicer_to_server`
# to add the defined class to the created server
sender_pb2_grpc.add_SenderServicer_to_server(
        SenderServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)