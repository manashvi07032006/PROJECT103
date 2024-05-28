import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/prade/Downloads"
to_dir = "C:/Users/prade/OneDrive/Desktop/Downloaded"

dir_tree = { "Music_Files": ['.mp3', '.mp4', '.wav'],
            "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], 
            "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
            "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], 
            "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")
        
    def on_deleted(self, event):
        print(f"Hey, {event.src_path} has been deleted")
        
    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified")
        
    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved")

event_handler = FileEventHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()