import time
from datetime import datetime
import socket
import threading
from concurrent.futures import ThreadPoolExecutor

# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

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


def banner_grab(sock, port):
    try:
        sock.settimeout(1)
        banner = sock.recv(1024).decode().strip()
        print(f"[DEBUG] Banner on port {port}: {banner}")
        return banner if banner else "No banner returned"
    except:
        return "No banner"
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if result == 0:
            banner = banner_grab(sock, port)
            msg = f"[{timestamp}] Port {port} is OPEN - {YELLOW}{banner}{RESET}"
            print(f"{GREEN}{msg}{RESET}")

            open_ports.append(port)

            with lock:
                with open("scan_results.txt", "a") as f:
                    f.write(f"[{timestamp}] Port {port} is OPEN - {banner}\n")
        else:
            print(f"{RED}[{timestamp}] Port {port} is CLOSED{RESET}")

        sock.close()

    except Exception as e:
        print(f"{RED}Error on port {port}: {e}{RESET}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        banner = banner_grab(sock, port)
        msg = f"[{timestamp}] Port {port} is OPEN - {YELLOW}{banner}{RESET}"
        print(f"{GREEN}{msg}{RESET}")

        open_ports.append(port)

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