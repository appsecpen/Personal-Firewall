import psutil
import socket
from datetime import datetime

# 🔒 Blocklist
BLOCKED_IPS = ['192.168.0.100', '127.0.0.1']
BLOCKED_PORTS = [80, 443]

def list_connections():
    print(f"{'Proto':<8}{'Local Address':<25}{'Remote Address':<25}{'Status':<15}{'Blocked?'}")
    print("-" * 100)

    with open("log.txt", "a") as logfile:
        for conn in psutil.net_connections(kind='inet'):
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            proto = 'TCP' if conn.type == socket.SOCK_STREAM else 'UDP' if conn.type == socket.SOCK_DGRAM else str(conn.type)

            blocked = False
            if conn.raddr and (conn.raddr.ip in BLOCKED_IPS or conn.raddr.port in BLOCKED_PORTS):
                blocked = True
                # Log blocked connections
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logfile.write(f"[{timestamp}] BLOCKED {proto} {laddr} -> {raddr} ({conn.status})\n")

            status_text = "Yes 🚫" if blocked else "No ✅"
            print(f"{proto:<8}{laddr:<25}{raddr:<25}{conn.status:<15}{status_text}")

if __name__ == "__main__":
    list_connections()
