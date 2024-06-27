#!/usr/bin/env python3
import subprocess
import re
import time
from datetime import datetime

def log_gpu_usage():
    # Command to get GPU utilization
    cmd = "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader"
    
    # Run the command
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    gpu_usage = result.stdout.strip()
    
    # Extract the numeric value of the GPU usage
    usage_percent = int(re.findall(r'\d+', gpu_usage)[0])
    
    # Check if usage is more than 50%
    if usage_percent > 50:
        # Log the high usage
        with open("gpu_usage_log.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"{timestamp} - GPU Usage: {usage_percent}%\n"
            file.write(log_message)
            print(log_message)  # Also print to console

def main():
    try:
        while True:
            log_gpu_usage()
            time.sleep(10)  # Check every 10 seconds
    except KeyboardInterrupt:
        print("Stopped GPU monitoring.")

if __name__ == "__main__":
    main()
