import os
import hashlib
import time
import json

# Directory to monitor
directory_to_monitor = "/home/kali/test_directory"

# Hash storage
state_file = "file_hashes.json"
file_hashes = {}

def load_hashes():
    """Load the hashes from a file if it exists."""
    global file_hashes
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            file_hashes = json.load(f)

def save_hashes():
    """Save the hashes to a file."""
    global file_hashes
    with open(state_file, "w") as f:
        json.dump(file_hashes, f)

def calculate_hash(file_path):
    """Calculate the SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def monitor_directory():
    """Monitor the directory for changes."""
    global file_hashes
    while True:
        current_files = {}
        for root, _, files in os.walk(directory_to_monitor):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = calculate_hash(file_path)
                current_files[file_path] = file_hash
                if file_path not in file_hashes:
                    print(f"New file added: {file_path}")
                elif file_hashes[file_path] != file_hash:
                    print(f"File modified: {file_path}")

        # Check for deleted files
        deleted_files = set(file_hashes) - set(current_files)
        for deleted_file in deleted_files:
            print(f"File deleted: {deleted_file}")

        # Update the hash storage and save state
        file_hashes = current_files
        save_hashes()

        time.sleep(5)  # Delay between checks

if __name__ == "__main__":
    print(f"Monitoring directory: {directory_to_monitor}")
    load_hashes()
    monitor_directory()
