# Raspberry Pi Network Manager

<p>
This Python script ensures that your Raspberry Pi stays connected to the internet. It monitors network connectivity and takes corrective actions, such as restarting the Wi-Fi interface (wlan0) or rebooting the system when necessary. It is especially useful for Raspberry Pi setups where constant network connectivity is critical, such as IoT devices or remote servers.
</p>

## Features

- Automatic Network Monitoring: Pings multiple hosts to check internet connectivity.
- Corrective Actions: Restarts the Wi-Fi interface or reboots the system based on the situation.
- Retry Mechanism: Retries the network check before taking any action to minimize unnecessary restarts or reboots.
- Log Cleanup: Automatically removes log files at midnight to prevent clutter.
- Customizable: Easily adapt the script to your specific needs by modifying parameters.

## Prerequisites

- A Raspberry Pi running Raspberry Pi OS.
- Python 3 installed (most Raspberry Pi OS versions come with Python 3 pre-installed).
- sudo permissions to allow the script to restart network services or reboot the system.

## Installation

### Step 1: Download the Script

Save the script as network_manager.py in your home directory or another location:

```
git clone https://github.com/mokhutsoane/Useful-Raspberry-pi-scripts.git

```

### Step 2: Make the Script Executable

Run the following command to make the script executable:

```
chmod +x ~/network_manager.py

```

### Step 3: Configure Cron Job

Set up a cron job to execute the script periodically:

Open the cron editor:

```
crontab -e

```

Add the following line to run the script every 5 minutes:

```
*/5 * * * * /home/pi/network_manager.py >> /home/pi/network_manager.log 2>&1

```

Replace /home/pi/ with the path where you saved the script if different.

## Contributions

Feel free to fork this repository and submit pull requests for improvements. Suggestions and bug reports are welcome!
