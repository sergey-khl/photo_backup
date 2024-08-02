import subprocess

if __name__ == "__main__":
    try:
        result = subprocess.run(['rclone', 'ls', 'mega_bear:'], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the rclone query: {e}")
