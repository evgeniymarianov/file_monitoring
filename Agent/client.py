import grpc
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# import the generated classes
import sender_pb2
import sender_pb2_grpc
import csv

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = sender_pb2_grpc.SenderStub(channel)

# create a valid request message
class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path)
        if '.csv' in str(event):
            with open(event.src_path) as new_csv:
                package = dict(csv.reader(new_csv))
                print(package)
            message = sender_pb2.Message(value=event.src_path)
            # make the call
            response = stub.Send(message)
            # et voilà
            print(response.value)


observer = Observer()
observer.schedule(Handler(), path='./observed_dir/', recursive=True)
observer.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
