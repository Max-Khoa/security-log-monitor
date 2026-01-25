FROM ubuntu:latest

# Alle Installationen + Git-Clone in EINER RUN (wichtig!)
RUN apt-get update && \
    apt-get install -y openssh-server git python3 python3-termcolor python3-pip && \
    mkdir /var/run/sshd && \
    git clone https://github.com/Max-Khoa/security-log-monitor.git /app && \
    cd /app && \
    pip3 install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# SSH konfigurieren
RUN echo 'root:password' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    ssh-keygen -A

# Working directory setzen
WORKDIR /app

# SSH Port freigeben
EXPOSE 22

# SSH Server starten (Foreground!)
CMD ["/usr/sbin/sshd", "-D"]
