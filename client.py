import sys
import time
import yaml
from watchdog.observers import Observer
from watchdog.events import *

config_file = "client.yml"

def get_config(index):
    with open(config_file) as f:
        return yaml.load(f, Loader=yaml.FullLoader)[index]

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        files = get_config("files")
        if event.src_path.replace("./", "") in files:
            print("log file %s changed!" % event.src_path)

if __name__ == "__main__":
    print("Monitored Files: " + str(get_config("files")))
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