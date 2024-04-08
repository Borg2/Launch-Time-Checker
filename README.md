Features:
- Measures the time taken to launch applications such as PowerPoint, WhatsApp, Code::Blocks, Google Chrome, and Microsoft 365.
- Utilizes psutil to check if the specified application processes are running.
- Utilizes pyautogui to simulate keyboard inputs and automate the process of launching applications.
- Outputs the launch time for each application to the console.

Dependencies:
- Python 3.x
- psutil library: https://github.com/giampaolo/psutil
- pyautogui library: https://github.com/asweigart/pyautogui

Usage:
1. Ensure Python 3.x is installed on your system.
2. Install the required dependencies using pip install psutil pyautogui.
3. Run the script using python main.py.
4. The script will launch each specified application and display the time taken to launch it.

Note:
- This script is designed to run on Windows systems.
- Ensure that the specified applications are installed and accessible via the system PATH.
