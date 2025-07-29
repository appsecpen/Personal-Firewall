🔥 Personal Firewall using Python
This project is part of the Elevate Labs Internship Program. It is a lightweight CLI-based personal firewall built using Python to monitor and block network connections based on defined IP and port rules.

📌 Project Objective
To develop a lightweight firewall that monitors real-time network connections and blocks suspicious traffic based on custom IP and port rules. This project helps understand system-level traffic monitoring, rule-based filtering, and basic security logging using Python.

👨‍💻 Features
- Lists all active TCP/UDP connections
- Detects and flags connections from blocked IPs or ports
- Logs blocked connections with timestamp to log.txt
- Simple command-line interface (CLI)
- Easy to customize blocklists

📁 Files Included
- File	- Description
- fire.py	- Lists all active connections using psutil
- fireblock.py -	Displays connection status and block info
- fireblock_log.py -	[Main Script] Logs blocked connections
- log.txt	- Auto-generated log file of blocked connections
- README.md -	Project overview and usage guide
- project_report.pdf -	Final report for internship submission

🛡️ Blocklist Example (Defined in Script)

BLOCKED_IPS = ['192.168.0.100', '127.0.0.1']
BLOCKED_PORTS = [80, 443]

🚀 How to Run
🔧 Step 1: Install Dependency

pip install psutil

🔧 Step 2: Run the Script
Choose any script based on your need:

- python fire.py            # List all active connections
- python fireblock.py       # Block and display flagged  connections
- python fireblock_log.py   # Block and log connections (Main Script)

📂 Output logs (if any) will be saved in log.txt

🧠 Concepts Explored
Network traffic monitoring

Firewall logic and rule-based filtering

System-level connection tracking with psutil

Logging and alerting mechanisms

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute it with attribution.

🙏 Acknowledgements
Elevate Labs – For the opportunity and internship platform

OWASP Top 10 – For inspiring the firewall logic and scanning features

Python community – For open-source tools and guidance

psutil – For enabling system-level process and network inspection

👩‍💻 Developer
Yawanikha (@appsecpen)
Cybersecurity Intern, Elevate Labs

