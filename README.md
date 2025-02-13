Endpoint-Keystroke-Monitor
This tool captures keystrokes and logs them to an output text file while running in the background.
Disclaimer

This tool is intended for ethical and authorized use only. Unauthorized use of this software to record keystrokes without explicit permission is illegal and may violate privacy laws. The developer assumes no responsibility for any misuse.

Overview

This keylogger is designed for authorized penetration testing and ethical security audits. It captures keystrokes and logs them to an output text file while running in the background. The tool includes an optional command prompt window displaying a custom ASCII signature and a disclaimer.

Features
Runs windowless in the background
Captures all keystrokes and saves them to an output file
Opens a separate cmd window for displaying an ASCII signature and ethical disclaimer
Works as a standalone executable
Designed for authorized security professionals

Installation
1. Download the executable (keylogger.exe).
2. Place the executable in a desired folder.
3. Double-click keylogger.exe to run it.
4. To stop the keylogger, close the background process from Task Manager.

Running from Source
1. Ensure you have Python 3.x installed.
2. Install required dependencies (if applicable):
   pip install pynput
3. Run the script:
   python keylogger.py

To compile it into an executable:
pyinstaller --onefile --noconsole keylogger.py

Usage
Log Output: Captured keystrokes will be saved in a text file (output.txt).
Signature Display: A separate command prompt window will show the ASCII signature and disclaimer.
Stopping the Keylogger: Close the background process or manually terminate it from Task Manager.

Legal Notice
Use this tool only with proper authorization. Unauthorized surveillance or keylogging is illegal and may result in severe consequences. By using this tool, you agree to comply with all applicable laws and regulations.
