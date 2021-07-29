import platform
import subprocess
import wmi
from datetime import datetime

import GPUtil
import psutil
from tabulate import tabulate


def basic_system_infor_cmd():
    info = {}
    my_system = platform.uname()
    __init__ = wmi.WMI()
    user_system = __init__.Win32_ComputerSystem()[0]

    os_ident = platform.system()
    info["OS"] = os_ident
    processor_details = platform.processor()
    info["Processor"] = processor_details
    architecture_details = platform.architecture()
    info["Architecture"] = architecture_details

    print("*" * 20 + " System Info " + "*" * 20)
    print(f"Manufacturer: {user_system.Manufacturer}")
    print(f"Model: {user_system.Model}")
    print(f"Name: {user_system.Name}")
    print("OS: " + info["OS"])
    print(f"Version: {my_system.version}")
    print("Processor: " + info["Processor"])
    print(f"SystemType: {user_system.SystemType}")
    print(f"SystemFamily: {user_system.SystemFamily}")


def system_infor_cmd():
    print("Please wait this may take a sec...")
    system = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    all_sys_info = []
    for info in system:
        all_sys_info.append(str(info.split("\r")[:-1]))
    for things in all_sys_info:
        print(things[2:-2])


def advanced_system_infor_cmd():
    def byte_sizes(byte, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if byte < factor:
                return f"{byte:.2f}{unit}{suffix}"
            byte /= factor

    # System Information(see "basic_system_infor")
    basic_system_infor_cmd()

    # Boot Information
    print("*" * 40, "Boot Time", "*" * 40)
    boot_time = psutil.boot_time()
    boot_time_conversion = datetime.fromtimestamp(boot_time)
    print(f"Boot Time: {boot_time_conversion.year}/{boot_time_conversion.month}/{boot_time_conversion.day}"
          f" {boot_time_conversion.hour}:{boot_time_conversion.minute}:{boot_time_conversion.second}")

    # Processor Information
    print("*" * 40, "CPU Information", "*" * 40)
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    processor_frequency = psutil.cpu_freq()
    print(f"Min Frequency: {processor_frequency.min:.2f}Mhz")
    print(f"Max Frequency: {processor_frequency.max:.2f}Mhz")
    print(f"Current Frequency: {processor_frequency.current:.2f}Mhz")
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i + 1}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    # Memory Information
    print("*" * 40, "Memory Information", "*" * 40)
    system_memory = psutil.virtual_memory()
    print(f"Used: {byte_sizes(system_memory.used)}/{byte_sizes(system_memory.total)}")
    print(f"Available: {byte_sizes(system_memory.available)}/{byte_sizes(system_memory.total)}")
    print(f"Percentage: {system_memory.percent}%/100%")
    print(f"Total: {byte_sizes(system_memory.total)}")

    # Swap Memory Information
    print("*" * 40, "Swap Memory", "*" * 40)
    swap = psutil.swap_memory()
    print(f"Total: {byte_sizes(swap.total)}")
    print(f"Free: {byte_sizes(swap.free)}/{byte_sizes(swap.total)}")
    print(f"Used: {byte_sizes(swap.used)}/{byte_sizes(swap.total)}")
    print(f"Percentage: {swap.percent}%/100%")

    # Disk Information
    print("*" * 40, "Disk Information", "*" * 40)
    print("Partitions and Usage:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"*** Device: {partition.device} ***")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            print("Access denied")
            continue
        print(f"  Total Size: {byte_sizes(partition_usage.total)}")
        print(f"  Used: {byte_sizes(partition_usage.used)}")
        print(f"  Free: {byte_sizes(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {byte_sizes(disk_io.read_bytes)}")
    print(f"Total write: {byte_sizes(disk_io.write_bytes)}")

    # Network Information
    print("*" * 40, "Network Information", "*" * 40)
    if_address = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_address.items():
        for address in interface_addresses:
            print(f"*** Interface: {interface_name} ***")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {byte_sizes(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {byte_sizes(net_io.bytes_recv)}")

    # GPU Information
    print("*" * 40, "GPU Information", "*" * 40)
    gpus = GPUtil.getGPUs()
    list_gpus_information = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load * 100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus_information.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    print(tabulate(list_gpus_information, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                                   "temperature", "uuid")))


def python_ver_cmd():
    print("Python 3.8.2[2020]")
