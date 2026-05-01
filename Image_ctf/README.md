# Challenge 1: Deleted Cat Evidence

## Category

Disk Forensics, File Recovery, Metadata Analysis

## Story

A user deleted an image from a small disk image before the evidence was collected. Investigators believe the image contained hidden information in its metadata.

You have been given the compressed forensic disk image. Recover the deleted evidence and find the hidden flag.

## Evidence Provided

```text
final.dd.xz
```

## Objective

Recover the deleted JPG image from the disk image and extract the flag hidden in the image metadata.

## Questions

1. What type of forensic artifact is provided?
2. Can you identify the partition inside the disk image?
3. Can you recover the deleted image file?
4. Which metadata field contains the hidden flag?
5. What is the final flag?

## Flag Format

```text
FLAG{...}
```

## Suggested Tools

```text
xz
mmls
foremost
exiftool
strings
grep
```
