# File Integrity Monitor (FIM)

The **File Integrity Monitor (FIM)** is a Python-based tool designed to detect unauthorized changes to files and directories in real time. It logs file additions, modifications, and deletions, ensuring data integrity and enhancing security. This tool is ideal for system administrators and security professionals seeking to monitor critical files.

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
