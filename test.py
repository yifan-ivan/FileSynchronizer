import sys
import logging
import time
from watchdog.observers import Observer
from watchdog.events import *

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("log file %s changed!" % event.src_path)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()