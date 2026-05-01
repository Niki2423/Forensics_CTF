FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        binutils \
        ca-certificates \
        coreutils \
        file \
        foremost \
        grep \
        libimage-exiftool-perl \
        sleuthkit \
        tshark \
        xz-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /ctf

COPY docker/README.md /ctf/README.md
COPY Image_ctf/README.md /ctf/challenges/image_metadata_disk_forensics/README.md
COPY Image_ctf/final.dd.xz /ctf/challenges/image_metadata_disk_forensics/final.dd.xz
COPY pcap_ctf/README.md /ctf/challenges/suspicious_network_traffic_pcap/README.md
COPY pcap_ctf/challenge.pcap /ctf/challenges/suspicious_network_traffic_pcap/challenge.pcap
COPY solutions/ /ctf/solutions/

CMD ["/bin/bash"]
