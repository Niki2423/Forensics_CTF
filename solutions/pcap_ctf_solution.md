# Solution: Suspicious Office Traffic

## Objective

Analyze `challenge.pcap`, identify the suspicious traffic, extract the encoded payload, and decode the flag.

## Steps

1. Go to the challenge folder:

```bash
cd /ctf/challenges/suspicious_network_traffic_pcap
```

2. Confirm the PCAP file exists:

```bash
ls -lh challenge.pcap
```

3. View IP conversations:

```bash
tshark -r challenge.pcap -q -z conv,ip
```

Important suspicious conversation:

```text
192.168.10.5 <-> 10.0.0.66
```

The suspicious internal host is `192.168.10.5`, and the external IP is `10.0.0.66`.

4. Check DNS traffic:

```bash
tshark -r challenge.pcap -Y dns -T fields -e frame.number -e ip.src -e ip.dst -e dns.qry.name
```

Expected result:

```text
5    192.168.10.5    8.8.8.8    sync-checker-update.com
```

The suspicious domain is `sync-checker-update.com`.

5. Find the encoded payload:

```bash
strings challenge.pcap | grep Rkx
```

Expected result:

```text
RkxBR3tuZXR3b3JrX2ZvcmVuc2ljc19jYXNlfQ==
```

6. Decode the payload:

```bash
echo "RkxBR3tuZXR3b3JrX2ZvcmVuc2ljc19jYXNlfQ==" | base64 -d
```

Expected result:

```text
FLAG{network_forensics_case}
```

## Flag

```text
FLAG{network_forensics_case}
```
