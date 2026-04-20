
---

# 2. `pcap_ctf/SOLUTION.md`

```md
# Solution — Suspicious Network Traffic PCAP Challenge

## Challenge Name
**Suspicious Office Traffic**

---

## Overview

This challenge simulates a small network forensics investigation. A packet capture was taken during an incident in which a workstation behaved suspiciously. The player must inspect the traffic, identify suspicious communication, and recover a flag hidden in an encoded network payload.

This challenge is related to **network forensics**, **protocol analysis**, **DNS investigation**, and **payload extraction**.

---

## Objective

Analyze the PCAP file, identify the compromised host, find the suspicious domain and external IP, inspect the traffic stream, and recover the hidden flag.

---

## Files Provided

- `challenge.pcap`

---

## Flag Format

```text
FLAG{...}
