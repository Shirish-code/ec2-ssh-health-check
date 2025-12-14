import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python ec2_health_check.py <host>")
    sys.exit(1)

host = sys.argv[1]
port = 22
timeout = 5

def check_ssh(host, port, timeout):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception as e:
        return False, str(e)

result = check_ssh(host, port, timeout)

if result is True:
    print(f"HEALTHY: {host} is reachable on port {port}")
else:
    print(f"UNHEALTHY: {host} not reachable on port {port}")
    print(f"Reason: {result[1]}")
