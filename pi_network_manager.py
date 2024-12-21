#!/usr/bin/env python3

import os
import subprocess
import time
from datetime import datetime

hosts_to_check = ["linphone.org", "google.com", "8.8.8.8"]


def remove_log_file(log_file):
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == "00:00:00" and os.path.exists(log_file):
        os.remove(log_file)
        print(f"{log_file} removed at midnight.")


def is_network_connected():
    for host in hosts_to_check:
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-w", "5", host],
                capture_output=True,
                text=True,
            )
            if "time=" in result.stdout:
                return True
        except Exception as e:
            print(f"Error pinging {host}: {e}")
    return False


def restart_wlan0():
    print("Broken connection, restarting wlan0 now.")
    subprocess.run(["/sbin/ifdown", "wlan0"])
    time.sleep(1)
    subprocess.run(["/sbin/ifup", "wlan0"])
    print("wlan0 restarted.")


def reboot_system():
    print("Rebooting the system now.")
    subprocess.run(["sudo", "/sbin/reboot"])


def main():
    print(datetime.now())

    for attempt in range(3):
        if is_network_connected():
            print("Network is connected.")
            return
        print(f"Network check attempt {attempt + 1} failed. Retrying...")
        time.sleep(10)
    current_time = datetime.now().strftime("%H:%M:%S")
    if int(current_time.split(":")[1]) % 10 == 0:
        print("Rebooting after multiple failed attempts.")
        reboot_system()
    else:
        print("Restarting wlan0 after multiple failed attempts.")
        restart_wlan0()


if __name__ == "__main__":
    main()
