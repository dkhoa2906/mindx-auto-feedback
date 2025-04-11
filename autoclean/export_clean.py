import os
import threading
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPORT_DIRS = [
    os.path.join(BASE_DIR, "docx_output"),
    os.path.join(BASE_DIR, "pdf_output"),
]

MAX_AGE_HOURS = 72

def cleanup_expired():
    now = time.time()
    for export_dir in EXPORT_DIRS:
        for filename in os.listdir(export_dir):
            file_path = os.path.join(export_dir, filename)
            if os.path.isfile(file_path):
                file_age = (now - os.path.getmtime(file_path)) / 3600
                if file_age > MAX_AGE_HOURS:
                    try:
                        os.remove(file_path)
                        print(f"Deleted old file: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")

def schedule_cleanup(interval=3600*12):  # every 12 hours
    def job():
        while True:
            cleanup_expired()
            time.sleep(interval)

    threading.Thread(target=job, daemon=True).start()
