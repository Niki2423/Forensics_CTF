from scapy.all import *
import base64

packets = []

# ---- Network Setup ----
victim = "192.168.10.5"
employee = "192.168.10.8"
gateway = "192.168.10.1"
dns_server = "8.8.8.8"
attacker_ip = "10.0.0.66"

# ---- 1. Normal Traffic ----
packets.append(
    IP(src=victim, dst="142.250.72.14") /
    TCP(dport=80) /
    Raw(load="GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n")
)

packets.append(
    IP(src=employee, dst="151.101.1.69") /
    TCP(dport=80) /
    Raw(load="GET /news HTTP/1.1\r\nHost: news.example.com\r\n\r\n")
)

# ---- 2. Internal Communication (story clue) ----
packets.append(
    IP(src=employee, dst=victim) /
    TCP(dport=5000) /
    Raw(load="Hey, your system is acting weird?")
)

packets.append(
    IP(src=victim, dst=employee) /
    TCP(dport=5000) /
    Raw(load="Yeah, I didn't send anything!")
)

# ---- 3. Suspicious DNS Query ----
packets.append(
    IP(src=victim, dst=dns_server) /
    UDP(dport=53) /
    DNS(rd=1, qd=DNSQR(qname="sync-checker-update.com"))
)

# ---- 4. Hidden Flag in HTTP POST ----
flag = "FLAG{network_forensics_case}"
encoded_flag = base64.b64encode(flag.encode()).decode()

packets.append(
    IP(src=victim, dst=attacker_ip) /
    TCP(dport=80) /
    Raw(load=(
        f"POST /upload HTTP/1.1\r\n"
        f"Host: sync-checker-update.com\r\n"
        f"Content-Type: text/plain\r\n\r\n"
        f"{encoded_flag}"
    ))
)

# ---- 5. Beaconing / repeated suspicious traffic ----
for i in range(3):
    packets.append(
        IP(src=victim, dst=attacker_ip) /
        TCP(dport=80) /
        Raw(load="PING")
    )

# ---- 6. Noise Traffic ----
for i in range(5):
    packets.append(
        IP(src="192.168.10.20", dst="192.168.10.30") /
        TCP(dport=443) /
        Raw(load="TLS DATA")
    )

# ---- Save PCAP ----
wrpcap("challenge.pcap", packets)

print("PCAP created: challenge.pcap")
