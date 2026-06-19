import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# The directory inside the container we want to watch
WATCH_DIRECTORY = os.environ.get("WATCH_DIRECTORY", "/app/docs")

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Prevent triggering on directories
        if event.is_directory:
            return
        
        print(f" New file detected: {event.src_path}")
        
        # --- YOUR PROCESSING LOGIC HERE ---
        # Example: Read the file, process data, etc.
        try:
            with open(event.src_path, 'r') as f:
                print(f"Processing content of {os.path.basename(event.src_path)}...")
                # do_something(f.read())
        except Exception as e:
            print(f"Error processing file: {e}")
        # ----------------------------------

if __name__ == "__main__":
    print("file-watcher running...")
    # Ensure the directory exists
    os.makedirs(WATCH_DIRECTORY, exist_ok=True)
    
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_DIRECTORY, recursive=False)
    
    print(f"🚀 Starting file watcher on {WATCH_DIRECTORY}...")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()