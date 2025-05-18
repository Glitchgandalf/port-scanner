import socket
import threading

print("Basic Port Scanner")

# Ask user for target and port range
target = input("Enter target IP (e.g., 127.0.0.1): ")
start_port = int(input("Enter start port (e.g., 1): "))
end_port = int(input("Enter end port (e.g., 1024): "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

# Loop through ports and scan
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        # You can hide this else if you want cleaner output
        # else:
        # print(f"Port {port} is closed")

        sock.close()
    except:
        pass  # Ignore failed scans

# Launch one thread per port
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()