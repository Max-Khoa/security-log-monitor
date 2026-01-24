# security-log-monitor
Python-based security log monitoring tool for detecting anomalies, error patterns, and potential attacks in server and application logs using rule-based checks and machine learning.

git clone git@github.com:Max-Khoa/security-log-monitor.git
cd security-log-monitor
docker-compose up -d --build

docker/
├── target/          # SSH-Server (testuser:pass123, admin:admin123)
├── attacker/        # Pentest tools (Hydra, Nmap, etc.)
└── docker-compose.yml

# 1. Start services
docker-compose up -d --build

# 2. Attack from attacker container
docker-compose exec attacker hydra -l testuser -P rockyou.txt ssh://target

# 3. See login attempts
tail -f logs/auth.log
