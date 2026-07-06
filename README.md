# Network Packet Sniffer

A Python-based network packet sniffer built using Scapy to capture and analyze network traffic.

## Features

- Captures live network packets
- Displays source and destination IP addresses
- Detects TCP, UDP, and ICMP protocols
- Displays source and destination ports
- Shows packet length and timestamp
- Detects HTTP (Port 80) and HTTPS (Port 443) traffic

## Requirements

- Python 3.x
- Scapy
- Npcap (Windows)

## Installation

1. Install Python.
2. Install Scapy:

```bash
pip install scapy
```

3. Install Npcap (Windows):
   - Download and install Npcap from https://npcap.com/
   - Enable **WinPcap API-compatible Mode** during installation.

## Run

```bash
python sniffer.py
```

## Technologies Used

- Python
- Scapy
- Npcap

## Project Output

The program captures live network packets and displays:
- Timestamp
- Source IP Address
- Destination IP Address
- Packet Length
- Protocol (TCP, UDP, ICMP)
- Source Port
- Destination Port
- HTTP and HTTPS traffic detection

## Author

**Jason Dsouza**
