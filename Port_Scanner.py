import time
from datetime import datetime
import socket
import threading
from concurrent.futures import ThreadPoolExecutor

print("Basic Port Scanner")

# Ask user for target and port range
target = input("Enter target IP (e.g., 127.0.0.1): ")
start_port = int(input("Enter start port (e.g., 1): "))
end_port = int(input("Enter end port (e.g., 1024): "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

# Open log file
output_file = open("scan_results.txt", "w")

start_time = time.time()
open_ports = []

# Lock to prevent threads from writing at the same time
lock = threading.Lock()


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msg = f"[{timestamp}] Port {port} is OPEN"
            print(f"{msg}")

            open_ports.append(port)  # Track open ports

            with lock:
                with open("scan_results.txt", "a") as f:
                    f.write(msg + "\n")

        sock.close()
    except:
        pass

# Limit to 100 concurrent threads (adjustable)
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))


    # Wait for all threads to finish
main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

# Calculate scan time
end_time = time.time()
duration = round(end_time - start_time, 2)

# Summary
print("\nScan Summary")
print(f"Open ports found: {len(open_ports)}")
print(f"Ports scanned: {end_port - start_port + 1}")
print(f"Duration: {duration} seconds")