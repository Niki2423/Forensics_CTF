# Solution: Deleted Cat Evidence

## Objective

Recover the deleted JPG from `final.dd.xz` and read the hidden flag from its metadata.

## Steps

1. Go to the challenge folder:

```bash
cd /ctf/challenges/image_metadata_disk_forensics
```

2. Confirm the evidence file exists:

```bash
ls -lh final.dd.xz
```

3. Create a working folder and decompress the disk image:

```bash
mkdir -p /ctf/work/image_ctf
xz -dc final.dd.xz > /ctf/work/image_ctf/final.dd
```

4. Inspect the disk image partition table:

```bash
mmls /ctf/work/image_ctf/final.dd
```

Important result:

```text
004:  000       0000000040   0000614359   0000614320   disk image
```

5. Recover deleted files:

```bash
foremost -i /ctf/work/image_ctf/final.dd -o /ctf/work/image_ctf/recovered
```

6. List the recovered JPG files:

```bash
ls /ctf/work/image_ctf/recovered/jpg
```

Expected recovered file:

```text
00110208.jpg
```

7. Read the recovered image metadata:

```bash
exiftool /ctf/work/image_ctf/recovered/jpg/00110208.jpg | grep -i "Comment"
```

Expected result:

```text
Comment                         : FLAG{Drunk_cat_is_here}
```

## Flag

```text
FLAG{Drunk_cat_is_here}
```
