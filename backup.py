import subprocess

if __name__ == "__main__":
    try:
        DEST="crypt_photos:mega_bear"

        command = f'rclone sync --fast-list --exclude ".thumbnails/**" -P ~/storage/dcim {DEST}'
        subprocess.run(command.split(' '), check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the rclone query: {e}")
