import socket

print("Basic Port Scanner")

# Ask user for target and port range
target = input("Enter target IP (e.g., 127.0.0.1): ")
start_port = int(input("Enter start port (e.g., 1): "))
end_port = int(input("Enter end port (e.g., 1024): "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

# Loop through ports and scan
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Timeout after 0.5 sec

    result = sock.connect_ex((target, port))  # 0 = open

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed")

    sock.close()