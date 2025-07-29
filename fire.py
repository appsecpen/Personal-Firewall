import psutil
import socket

def list_connections():
    print(f"{'Proto':<8}{'Local Address':<25}{'Remote Address':<25}{'Status':<15}")
    print("-" * 80)

    for conn in psutil.net_connections(kind='inet'):
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        proto = 'TCP' if conn.type == socket.SOCK_STREAM else 'UDP' if conn.type == socket.SOCK_DGRAM else str(conn.type)
        print(f"{proto:<8}{laddr:<25}{raddr:<25}{conn.status:<15}")

if __name__ == "__main__":
    list_connections()
