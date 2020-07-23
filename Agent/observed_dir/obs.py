from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from greeting import say_hi

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path)
        if '.test' in str(event):
        	say_hi()

observer = Observer()
observer.schedule(Handler(), path='.', recursive=True)
observer.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
observer.join()