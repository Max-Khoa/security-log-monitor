FROM debian:bookworm-slim

# SSH-Server
RUN apt-get update && apt-get install -y \
    openssh-server \
    logrotate \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /var/run/sshd

# User für Tests
RUN useradd -m -s /bin/bash testuser && echo "testuser:pass123" | chpasswd
RUN useradd -m -s /bin/bash admin && echo "admin:admin123" | chpasswd

# SSH starten
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
