# 🔍 Python Port Scanner

A simple command-line port scanner built in Python using sockets.  
Great for learning the basics of networking and cybersecurity tools.

---

## Features

- Scan any IP or hostname
- Choose your own port range
- Detect open vs. closed ports
- Customizable timeout speed

---

## How It Works

The scanner:
1. Takes a target IP or domain from the user
2. Iterates over a range of ports
3. Attempts a TCP connection to each port
4. Reports which ports are open

---

## Example Usage

```bash
$ python3 Port_Scanner.py
Enter target IP (e.g., 127.0.0.1): 127.0.0.1
Enter start port (e.g., 1): 75
Enter end port (e.g., 85):

Scanning 127.0.0.1 from port 75 to 85...

Port 75 is closed
Port 76 is closed
Port 80 is OPEN

# Educational Value

This tool teaches:
	•	Network scanning fundamentals
	•	How TCP ports work
	•	Practical Python for cybersecurity