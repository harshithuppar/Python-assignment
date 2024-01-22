import psutil
import time

def monitor_cpu(threshold):
    print("Monitoring CPU usage...")
    
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)

            if cpu_percent > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_percent}%")

    #error handling
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Assigning threshold
    threshold = 80

    # calling funtion
    monitor_cpu(threshold)