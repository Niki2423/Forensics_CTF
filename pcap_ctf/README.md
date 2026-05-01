# Challenge 2: Suspicious Office Traffic

## Category

Network Forensics, PCAP Analysis, DNS Investigation, Payload Decoding

## Story

A workstation in an office network behaved suspiciously. A packet capture was collected during the incident. Investigators believe the host contacted suspicious infrastructure and sent hidden data over the network.

You have been given the PCAP file. Analyze the traffic and recover the hidden flag.

## Evidence Provided

```text
challenge.pcap
```

## Objective

Identify the suspicious communication, find the suspicious DNS request, extract the encoded payload, and decode the final flag.

## Questions

1. Which internal host appears suspicious?
2. Which external IP address does it communicate with?
3. What suspicious domain is queried?
4. What encoded payload is hidden in the PCAP?
5. What is the final decoded flag?

## Flag Format

```text
FLAG{...}
```

## Suggested Tools

```text
tshark
strings
grep
base64
```
