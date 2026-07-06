from scapy.all import *
from datetime import datetime

def packet_callback(packet):
    # Get current time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check if packet has IP layer
    if packet.haslayer(IP):
        ip = packet[IP]

        print("\n" + "=" * 60)
        print(f"Time           : {timestamp}")
        print(f"Source IP      : {ip.src}")
        print(f"Destination IP : {ip.dst}")
        print(f"Packet Length  : {len(packet)} bytes")

        # TCP Packet
        if packet.haslayer(TCP):
            tcp = packet[TCP]
            print("Protocol       : TCP")
            print(f"Source Port    : {tcp.sport}")
            print(f"Destination Port : {tcp.dport}")

            if tcp.dport == 80:
                print("HTTP Request Detected!")

            elif tcp.dport == 443:
                print("HTTPS Traffic Detected!")

        # UDP Packet
        elif packet.haslayer(UDP):
            udp = packet[UDP]
            print("Protocol: UDP")
            print(f"Source Port :{udp.sport}")
            print(f"Destination Port : {udp.dport}")

        # ICMP Packet
        elif packet.haslayer(ICMP):
            print("Protocol :ICMP")

        # Other Protocol
        else:
            print("Protocol:Other")

        print("=" * 60)

# Start sniffing
print("==========================================")
print("     Network Packet Sniffer Started")
print("     Press Ctrl + C to Stop")
print("==========================================")

sniff(prn=packet_callback, store=False)