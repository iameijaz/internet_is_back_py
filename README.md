# Internet Checker App

This is a simple Python application that checks for internet connectivity and plays a sound when the internet is back. It also allows you to measure the internet speed. The application uses the Tkinter library for the user interface.

## Features

- Automatically checks for internet connectivity when the application starts.
- Displays the status of the internet connection with color indicators:
  - Red: Not Connected
  - Orange: Checking...
  - Green: Connected
  - Blue: Measuring Speed...
- Option to play a sound when the internet is back.
- Measure internet speed (download and upload).

## Requirements

- Python 3.x
- The following Python packages:
  - `requests`
  - `playsound`
  - `tkinter` (usually included with Python installations)
  - `speedtest-cli`

## Installation

1. Clone the repository or download the source code.
2. Install the required packages:
   ```bash
   pip install requests playsound speedtest-cli
Usage
Place a sound file named sound.mp3 in the same directory as the script. You can use any other sound file and update the script with the correct file name.
Run the application:

`python internet_check.py`
