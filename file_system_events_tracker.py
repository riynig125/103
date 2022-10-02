from cgitb import handler
import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
source = "/Users/Space/Desktop/pro"
class fileEvent(FileSystemEventHandler):
    def on_created(self,event):
       print("file has been created")
    def on_deleted(self,event):
       print("file has been deleted")
    def on_modified(self,event):
       print("file has been modified")
    def on_moved(self,event):
       print("file has been moved")

event_handler = fileEvent()
observer = Observer()
observer.schedule(event_handler,source,recursive = True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stopped()