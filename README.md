# File Integrity Monitor (FIM)

The **File Integrity Monitor (FIM)** is a Python-based tool designed to detect unauthorised changes to files and directories in real time. It logs file additions, modifications, and deletions, ensuring data integrity and enhancing security. This tool is ideal for system administrators and security professionals seeking to monitor critical files.

---

## Features
- Tracks changes in specified directories.
- Detects:
  - **New files** added.
  - **File modifications**.
  - **File deletions**.
- Logs events in real time.
- Persistent state management:
  - Uses a JSON file to store file hashes, enabling detection across script restarts.
- Lightweight and easy to configure.

---

## Requirements
- **Python 3**: Ensure Python 3 is installed on your system.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Cyberlayers/file_integrity_monitor.git
   cd file_integrity_monitor
2. Ensure Python is installed:
   sudo apt update
   sudo apt install python3

---

## Usage Instructions
1. Run the tool
python3 file_integrity_monitor.py
2. Add a file:
  echo "New test file" > /home/kali/test_directory/new_file.txt
3. Modify a file
   echo "Modified content" >> /home/kali/test_directory/new_file.txt
4. Delete a file
   rm /home/kali/test_directory/new_file.txt
5. Observe the output for real-time logging of changes.

---

## Limitations
1. Monitors only one directory at a time (subdirectories included).
2. Relies on Python’s SHA256 hashing, which may affect performance for large files or directories.

---

## Disclaimer
This tool is intended for educational purposes and authorized use only. Unauthorized monitoring of systems you do not own or have explicit permission to access is illegal and unethical. The authors are not responsible for misuse.

---

## License
No license has been applied to this project. Usage, modification, or redistribution of the code requires explicit permission from the author.





