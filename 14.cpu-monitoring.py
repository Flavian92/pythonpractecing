#This Python script uses the psutil library to retrieve and display system-related information, such as CPU usage, memory usage, disk usage, and details about running processes.
# This script is useful for monitoring system resource usage and obtaining information about running processes. 
# It provides a snapshot of the system's current state at the time the script is executed.

import psutil


def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent


def get_memory_usage():
    memory = psutil.virtual_memory()
    total_memory = memory.total // (1024**3)  # Convert to GB
    used_memory = memory.used // (1024**3)
    memory_percent = memory.percent
    return total_memory, used_memory, memory_percent


def get_disk_usage():
    disk = psutil.disk_usage("/")
    total_space = disk.total // (1024**3)  # Convert to GB
    used_space = disk.used // (1024**3)
    disk_percent = disk.percent
    return total_space, used_space, disk_percent


def get_process_details():
    processes = []
    for proc in psutil.process_iter(["pid", "name", "username"]):
        processes.append(
            {
                "pid": proc.info["pid"],
                "name": proc.info["name"],
                "username": proc.info["username"],
            }
        )
    return processes


# Get system details
cpu_usage = get_cpu_usage()
total_memory, used_memory, memory_percent = get_memory_usage()
total_space, used_space, disk_percent = get_disk_usage()
processes = get_process_details()

# Print system details
print("CPU Usage:", cpu_usage)
print("Memory Usage:", f"{used_memory} GB / {total_memory} GB ({memory_percent}%)")
print("Disk Usage:", f"{used_space} GB / {total_space} GB ({disk_percent}%)")
print("Process Details:")
for process in processes:
    print(
        f"PID: {process['pid']}, Name: {process['name']}, User: {process['username']}"
    )
