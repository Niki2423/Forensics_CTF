# Digital Forensics CTF Lab

Welcome to the Docker version of the Digital Forensics CTF lab.

## Challenges

There are two challenges in this container:

```text
/ctf/challenges/image_metadata_disk_forensics
/ctf/challenges/suspicious_network_traffic_pcap
```

Each challenge folder contains a `README.md` with the story, objective, evidence file, and questions to answer.

## Solutions

Solutions are included here:

```text
/ctf/solutions
```

Try the challenges first, then open the solution files if you get stuck or need to verify your answer.

## Useful Commands

```bash
ls -R /ctf
cat /ctf/challenges/image_metadata_disk_forensics/README.md
cat /ctf/challenges/suspicious_network_traffic_pcap/README.md
```

## Installed Tools

```text
xz
mmls
foremost
exiftool
tshark
strings
grep
base64
file
```

## Flag Format

```text
FLAG{...}
```
