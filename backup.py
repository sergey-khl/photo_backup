import os
import logging
from datetime import datetime
import subprocess

log_filename = os.path.join("logs", f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        DEST="crypt_photos:mega_bear"

        command = f'rclone sync --fast-list --exclude ".thumbnails/**" -P ~/storage/dcim {DEST}'
        out = subprocess.run(command, capture_output=True, text=True, shell=True)
        logging.info(out.stderr)
        logging.info(out.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred during the rclone query: {e}")
